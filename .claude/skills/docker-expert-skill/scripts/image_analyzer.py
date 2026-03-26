#!/usr/bin/env python3
"""
Docker Image Layer Analyzer
Analyzes Docker image layers to identify optimization opportunities.
Run: python image_analyzer.py <image:tag>
"""

import subprocess
import json
import sys
import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Layer:
    """Represents a Docker image layer."""
    created_by: str
    size_bytes: int
    size_human: str
    comment: str = ""
    
    @property
    def is_large(self) -> bool:
        """Check if layer is considered large (>50MB)."""
        return self.size_bytes > 50 * 1024 * 1024
    
    @property
    def instruction(self) -> str:
        """Extract the Dockerfile instruction."""
        if self.created_by.startswith("/bin/sh -c"):
            return "RUN"
        for cmd in ["COPY", "ADD", "ENV", "WORKDIR", "USER", "EXPOSE", "CMD", "ENTRYPOINT"]:
            if cmd in self.created_by.upper():
                return cmd
        return "UNKNOWN"


def parse_size(size_str: str) -> int:
    """Parse human-readable size to bytes."""
    size_str = size_str.strip().upper()
    
    multipliers = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4,
    }
    
    match = re.match(r'^([\d.]+)\s*([A-Z]+)$', size_str)
    if match:
        value = float(match.group(1))
        unit = match.group(2)
        return int(value * multipliers.get(unit, 1))
    
    return 0


def get_image_history(image: str) -> list[Layer]:
    """Get image history as list of layers."""
    cmd = [
        "docker", "history", image,
        "--format", '{{.CreatedBy}}\t{{.Size}}\t{{.Comment}}',
        "--no-trunc"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}", file=sys.stderr)
        return []
    
    layers = []
    for line in result.stdout.strip().split('\n'):
        if not line.strip():
            continue
        
        parts = line.split('\t')
        created_by = parts[0] if len(parts) > 0 else ""
        size_str = parts[1] if len(parts) > 1 else "0B"
        comment = parts[2] if len(parts) > 2 else ""
        
        layers.append(Layer(
            created_by=created_by,
            size_bytes=parse_size(size_str),
            size_human=size_str,
            comment=comment
        ))
    
    return layers


def get_image_info(image: str) -> dict:
    """Get image metadata."""
    cmd = ["docker", "image", "inspect", image]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        return {"error": result.stderr}
    
    try:
        data = json.loads(result.stdout)
        if data:
            return data[0]
    except json.JSONDecodeError:
        pass
    
    return {}


def analyze_layers(layers: list[Layer]) -> dict:
    """Analyze layers for optimization opportunities."""
    total_size = sum(l.size_bytes for l in layers)
    large_layers = [l for l in layers if l.is_large]
    
    # Count instructions
    instruction_counts = {}
    for layer in layers:
        inst = layer.instruction
        instruction_counts[inst] = instruction_counts.get(inst, 0) + 1
    
    # Look for optimization opportunities
    opportunities = []
    
    # Check for multiple consecutive RUN commands
    run_count = instruction_counts.get("RUN", 0)
    if run_count > 5:
        opportunities.append({
            "type": "multiple_run",
            "message": f"Found {run_count} RUN instructions. Consider combining related commands.",
            "severity": "medium"
        })
    
    # Check for large layers
    for i, layer in enumerate(layers):
        if layer.is_large:
            opportunities.append({
                "type": "large_layer",
                "message": f"Layer {i+1} is {layer.size_human}: {layer.created_by[:80]}...",
                "severity": "info"
            })
    
    # Check for cache-busting patterns
    for layer in layers:
        if "apt-get update" in layer.created_by and "rm -rf /var/lib/apt" not in layer.created_by:
            opportunities.append({
                "type": "apt_cache",
                "message": "apt-get update without cleanup. Add: rm -rf /var/lib/apt/lists/*",
                "severity": "high"
            })
            break
    
    # Check for pip cache
    for layer in layers:
        if "pip install" in layer.created_by and "--no-cache-dir" not in layer.created_by:
            if "--mount=type=cache" not in layer.created_by:
                opportunities.append({
                    "type": "pip_cache",
                    "message": "pip install without --no-cache-dir or cache mount",
                    "severity": "medium"
                })
            break
    
    return {
        "total_size_bytes": total_size,
        "total_size_human": format_size(total_size),
        "layer_count": len(layers),
        "large_layer_count": len(large_layers),
        "instruction_counts": instruction_counts,
        "opportunities": opportunities
    }


def format_size(bytes_size: int) -> str:
    """Format bytes to human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} PB"


def print_analysis(image: str, layers: list[Layer], analysis: dict, info: dict):
    """Print analysis results."""
    print("=" * 70)
    print(f"IMAGE ANALYSIS: {image}")
    print("=" * 70)
    print()
    
    # Basic info
    print(f"Total Size: {analysis['total_size_human']}")
    print(f"Layer Count: {analysis['layer_count']}")
    print(f"Large Layers (>50MB): {analysis['large_layer_count']}")
    print()
    
    # Image metadata
    if info and "error" not in info:
        print("Image Metadata:")
        print(f"  Created: {info.get('Created', 'Unknown')[:19]}")
        print(f"  Architecture: {info.get('Architecture', 'Unknown')}")
        if info.get("Config", {}).get("Labels"):
            print(f"  Labels: {len(info['Config']['Labels'])} labels")
    print()
    
    # Instruction breakdown
    print("Instruction Breakdown:")
    for inst, count in sorted(analysis['instruction_counts'].items(), key=lambda x: -x[1]):
        print(f"  {inst}: {count}")
    print()
    
    # Layer details (top 10 by size)
    print("Top 10 Layers by Size:")
    sorted_layers = sorted(layers, key=lambda x: x.size_bytes, reverse=True)[:10]
    for i, layer in enumerate(sorted_layers, 1):
        cmd_preview = layer.created_by[:60] + "..." if len(layer.created_by) > 60 else layer.created_by
        print(f"  {i}. {layer.size_human:>10} | {cmd_preview}")
    print()
    
    # Optimization opportunities
    if analysis['opportunities']:
        print("Optimization Opportunities:")
        for opp in analysis['opportunities']:
            severity_icon = {"high": "🔴", "medium": "🟡", "info": "🔵"}.get(opp['severity'], "⚪")
            print(f"  {severity_icon} [{opp['type']}] {opp['message']}")
    else:
        print("✅ No obvious optimization opportunities found")
    
    print()
    print("=" * 70)


def main():
    if len(sys.argv) < 2:
        print("Usage: python image_analyzer.py <image:tag>")
        print("Example: python image_analyzer.py python:3.11-slim")
        sys.exit(1)
    
    image = sys.argv[1]
    
    print(f"Analyzing image: {image}...")
    print()
    
    layers = get_image_history(image)
    if not layers:
        print(f"Error: Could not get history for image '{image}'")
        print("Make sure the image exists locally (docker pull first)")
        sys.exit(1)
    
    info = get_image_info(image)
    analysis = analyze_layers(layers)
    
    if "--json" in sys.argv:
        output = {
            "image": image,
            "info": info if "error" not in info else None,
            "analysis": analysis,
            "layers": [
                {
                    "created_by": l.created_by,
                    "size_bytes": l.size_bytes,
                    "size_human": l.size_human,
                    "instruction": l.instruction
                }
                for l in layers
            ]
        }
        print(json.dumps(output, indent=2))
    else:
        print_analysis(image, layers, analysis, info)


if __name__ == "__main__":
    main()
