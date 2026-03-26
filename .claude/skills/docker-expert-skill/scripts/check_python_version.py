#!/usr/bin/env python3
"""
Python Version Checker
Extracts Python version requirements from project files.
Run: python check_python_version.py [project_path]
"""

import re
import sys
import json
from pathlib import Path
from typing import Optional


def check_pyproject_toml(path: Path) -> Optional[str]:
    """Extract Python version from pyproject.toml."""
    pyproject = path / "pyproject.toml"
    if not pyproject.exists():
        return None
    
    content = pyproject.read_text()
    
    # Check requires-python
    match = re.search(r'requires-python\s*=\s*["\']([^"\']+)["\']', content)
    if match:
        return match.group(1)
    
    # Check python in dependencies (Poetry style)
    match = re.search(r'python\s*=\s*["\']([^"\']+)["\']', content)
    if match:
        return match.group(1)
    
    return None


def check_setup_py(path: Path) -> Optional[str]:
    """Extract Python version from setup.py."""
    setup_py = path / "setup.py"
    if not setup_py.exists():
        return None
    
    content = setup_py.read_text()
    
    # Check python_requires
    match = re.search(r'python_requires\s*=\s*["\']([^"\']+)["\']', content)
    if match:
        return match.group(1)
    
    return None


def check_setup_cfg(path: Path) -> Optional[str]:
    """Extract Python version from setup.cfg."""
    setup_cfg = path / "setup.cfg"
    if not setup_cfg.exists():
        return None
    
    content = setup_cfg.read_text()
    
    match = re.search(r'python_requires\s*=\s*(.+)', content)
    if match:
        return match.group(1).strip()
    
    return None


def check_runtime_txt(path: Path) -> Optional[str]:
    """Extract Python version from runtime.txt (Heroku style)."""
    runtime = path / "runtime.txt"
    if not runtime.exists():
        return None
    
    content = runtime.read_text().strip()
    match = re.search(r'python-(\d+\.\d+(?:\.\d+)?)', content)
    if match:
        return match.group(1)
    
    return None


def check_python_version_file(path: Path) -> Optional[str]:
    """Extract Python version from .python-version (pyenv style)."""
    version_file = path / ".python-version"
    if not version_file.exists():
        return None
    
    return version_file.read_text().strip()


def check_dockerfile(path: Path) -> Optional[str]:
    """Extract Python version from existing Dockerfile."""
    for dockerfile in ["Dockerfile", "Dockerfile.dev", "Dockerfile.prod"]:
        df_path = path / dockerfile
        if df_path.exists():
            content = df_path.read_text()
            match = re.search(r'FROM\s+python:(\d+\.\d+)', content)
            if match:
                return f"={match.group(1)} (from {dockerfile})"
    
    return None


def parse_version_constraint(constraint: str) -> dict:
    """Parse version constraint to get min/max versions."""
    result = {
        "raw": constraint,
        "min_version": None,
        "max_version": None,
        "recommended": None
    }
    
    # Handle caret (^3.11)
    if constraint.startswith("^"):
        version = constraint[1:]
        parts = version.split(".")
        result["min_version"] = version
        if len(parts) >= 2:
            result["max_version"] = f"{parts[0]}.{int(parts[1]) + 1}"
            result["recommended"] = version
    
    # Handle tilde (~3.11)
    elif constraint.startswith("~"):
        version = constraint[1:]
        result["min_version"] = version
        result["recommended"] = version
    
    # Handle >=
    elif ">=" in constraint:
        match = re.search(r'>=\s*(\d+\.\d+)', constraint)
        if match:
            result["min_version"] = match.group(1)
            result["recommended"] = match.group(1)
    
    # Handle ==
    elif "==" in constraint:
        match = re.search(r'==\s*(\d+\.\d+(?:\.\d+)?)', constraint)
        if match:
            result["min_version"] = match.group(1)
            result["max_version"] = match.group(1)
            result["recommended"] = match.group(1)
    
    # Plain version
    else:
        match = re.search(r'(\d+\.\d+)', constraint)
        if match:
            result["recommended"] = match.group(1)
    
    return result


def get_docker_base_image(version: str) -> str:
    """Suggest Docker base image for Python version."""
    # Extract major.minor
    match = re.search(r'(\d+\.\d+)', version)
    if not match:
        return "python:3.11-slim-bookworm"
    
    py_version = match.group(1)
    
    # Map to recommended base images
    base_images = {
        "3.13": "python:3.13-slim-bookworm",
        "3.12": "python:3.12-slim-bookworm",
        "3.11": "python:3.11-slim-bookworm",
        "3.10": "python:3.10-slim-bookworm",
        "3.9": "python:3.9-slim-bookworm",
    }
    
    return base_images.get(py_version, f"python:{py_version}-slim-bookworm")


def main():
    project_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    
    if not project_path.exists():
        print(f"Error: Path '{project_path}' does not exist")
        sys.exit(1)
    
    results = {
        "path": str(project_path.absolute()),
        "sources": {},
        "recommendation": None
    }
    
    # Check all sources
    checkers = [
        ("pyproject.toml", check_pyproject_toml),
        ("setup.py", check_setup_py),
        ("setup.cfg", check_setup_cfg),
        ("runtime.txt", check_runtime_txt),
        (".python-version", check_python_version_file),
        ("Dockerfile", check_dockerfile),
    ]
    
    for name, checker in checkers:
        version = checker(project_path)
        if version:
            results["sources"][name] = version
    
    # Determine recommendation
    if results["sources"]:
        # Prefer pyproject.toml
        for source in ["pyproject.toml", ".python-version", "setup.py", "runtime.txt"]:
            if source in results["sources"]:
                constraint = results["sources"][source]
                parsed = parse_version_constraint(constraint)
                if parsed["recommended"]:
                    results["recommendation"] = {
                        "version": parsed["recommended"],
                        "base_image": get_docker_base_image(parsed["recommended"]),
                        "source": source,
                        "constraint": constraint
                    }
                    break
    
    # Output
    if "--json" in sys.argv:
        print(json.dumps(results, indent=2))
    else:
        print("=" * 50)
        print("PYTHON VERSION CHECK")
        print("=" * 50)
        print(f"Project: {results['path']}")
        print()
        
        if results["sources"]:
            print("Found versions:")
            for source, version in results["sources"].items():
                print(f"  {source}: {version}")
            print()
        else:
            print("No Python version requirements found.")
            print()
        
        if results["recommendation"]:
            rec = results["recommendation"]
            print("Recommendation:")
            print(f"  Python Version: {rec['version']}")
            print(f"  Docker Base Image: {rec['base_image']}")
            print(f"  Source: {rec['source']}")
        else:
            print("Recommendation:")
            print("  Python Version: 3.11 (default)")
            print("  Docker Base Image: python:3.11-slim-bookworm")
            print("  Note: No version constraint found, using safe default")
        
        print()
        print("=" * 50)


if __name__ == "__main__":
    main()
