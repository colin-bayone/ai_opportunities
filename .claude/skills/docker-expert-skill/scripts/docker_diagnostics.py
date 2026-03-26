#!/usr/bin/env python3
"""
Docker Diagnostics Script
Provides comprehensive Docker environment analysis.
Run: python docker_diagnostics.py [--json]
"""

import subprocess
import json
import sys
from datetime import datetime
from pathlib import Path


def run_cmd(cmd: list[str], capture: bool = True) -> tuple[int, str, str]:
    """Run a command and return (returncode, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=capture,
            text=True,
            timeout=30
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out"
    except FileNotFoundError:
        return -1, "", f"Command not found: {cmd[0]}"


def get_docker_version() -> dict:
    """Get Docker version information."""
    code, out, err = run_cmd(["docker", "version", "--format", "json"])
    if code == 0:
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            pass
    return {"error": err or "Failed to get Docker version"}


def get_docker_info() -> dict:
    """Get Docker system information."""
    code, out, err = run_cmd(["docker", "info", "--format", "json"])
    if code == 0:
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            pass
    return {"error": err or "Failed to get Docker info"}


def get_running_containers() -> list[dict]:
    """Get list of running containers."""
    code, out, err = run_cmd([
        "docker", "ps", "--format",
        '{"id":"{{.ID}}","name":"{{.Names}}","image":"{{.Image}}","status":"{{.Status}}","ports":"{{.Ports}}"}'
    ])
    if code == 0 and out:
        containers = []
        for line in out.split('\n'):
            if line.strip():
                try:
                    containers.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return containers
    return []


def get_all_containers() -> list[dict]:
    """Get list of all containers including stopped."""
    code, out, err = run_cmd([
        "docker", "ps", "-a", "--format",
        '{"id":"{{.ID}}","name":"{{.Names}}","image":"{{.Image}}","status":"{{.Status}}","created":"{{.CreatedAt}}"}'
    ])
    if code == 0 and out:
        containers = []
        for line in out.split('\n'):
            if line.strip():
                try:
                    containers.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return containers
    return []


def get_images() -> list[dict]:
    """Get list of Docker images."""
    code, out, err = run_cmd([
        "docker", "images", "--format",
        '{"repository":"{{.Repository}}","tag":"{{.Tag}}","id":"{{.ID}}","size":"{{.Size}}","created":"{{.CreatedAt}}"}'
    ])
    if code == 0 and out:
        images = []
        for line in out.split('\n'):
            if line.strip():
                try:
                    images.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return images
    return []


def get_volumes() -> list[dict]:
    """Get list of Docker volumes."""
    code, out, err = run_cmd([
        "docker", "volume", "ls", "--format",
        '{"name":"{{.Name}}","driver":"{{.Driver}}","scope":"{{.Scope}}"}'
    ])
    if code == 0 and out:
        volumes = []
        for line in out.split('\n'):
            if line.strip():
                try:
                    volumes.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return volumes
    return []


def get_networks() -> list[dict]:
    """Get list of Docker networks."""
    code, out, err = run_cmd([
        "docker", "network", "ls", "--format",
        '{"name":"{{.Name}}","driver":"{{.Driver}}","scope":"{{.Scope}}"}'
    ])
    if code == 0 and out:
        networks = []
        for line in out.split('\n'):
            if line.strip():
                try:
                    networks.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return networks
    return []


def get_disk_usage() -> dict:
    """Get Docker disk usage."""
    code, out, err = run_cmd(["docker", "system", "df", "--format", "json"])
    if code == 0:
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            # Try parsing text output
            code2, out2, _ = run_cmd(["docker", "system", "df"])
            return {"raw_output": out2}
    return {"error": err}


def check_compose_version() -> dict:
    """Check Docker Compose version."""
    # Try v2 first
    code, out, err = run_cmd(["docker", "compose", "version", "--short"])
    if code == 0:
        return {"version": out, "command": "docker compose", "v2": True}
    
    # Try legacy
    code, out, err = run_cmd(["docker-compose", "version", "--short"])
    if code == 0:
        return {"version": out, "command": "docker-compose", "v2": False, "warning": "Using legacy docker-compose"}
    
    return {"error": "Docker Compose not found"}


def check_buildkit() -> dict:
    """Check BuildKit status."""
    info = get_docker_info()
    if "error" in info:
        return {"error": info["error"]}
    
    # Check if BuildKit is default
    buildkit_enabled = info.get("BuildkitVersion", "") != ""
    
    return {
        "buildkit_version": info.get("BuildkitVersion", "Not available"),
        "enabled_by_default": buildkit_enabled,
        "docker_version": info.get("ServerVersion", "Unknown")
    }


def analyze_compose_file(path: str = ".") -> dict:
    """Analyze compose file in the given path."""
    compose_files = ["compose.yaml", "compose.yml", "docker-compose.yaml", "docker-compose.yml"]
    found_file = None
    
    for filename in compose_files:
        filepath = Path(path) / filename
        if filepath.exists():
            found_file = filepath
            break
    
    if not found_file:
        return {"found": False, "message": "No compose file found"}
    
    code, out, err = run_cmd(["docker", "compose", "-f", str(found_file), "config", "--services"])
    
    result = {
        "found": True,
        "file": str(found_file),
        "services": out.split('\n') if code == 0 else [],
    }
    
    # Check for deprecated version key
    with open(found_file) as f:
        content = f.read()
        if content.strip().startswith("version:") or "\nversion:" in content:
            result["warning"] = "Contains deprecated 'version' key - remove it"
    
    return result


def run_full_diagnostics() -> dict:
    """Run full Docker diagnostics."""
    return {
        "timestamp": datetime.now().isoformat(),
        "docker_version": get_docker_version(),
        "buildkit": check_buildkit(),
        "compose": check_compose_version(),
        "running_containers": get_running_containers(),
        "all_containers": get_all_containers(),
        "images": get_images(),
        "volumes": get_volumes(),
        "networks": get_networks(),
        "disk_usage": get_disk_usage(),
        "compose_file": analyze_compose_file(),
    }


def print_summary(diagnostics: dict):
    """Print human-readable summary."""
    print("=" * 60)
    print("DOCKER DIAGNOSTICS SUMMARY")
    print("=" * 60)
    print(f"Timestamp: {diagnostics['timestamp']}")
    print()
    
    # Docker Version
    version_info = diagnostics.get("docker_version", {})
    if "error" not in version_info:
        client_ver = version_info.get("Client", {}).get("Version", "Unknown")
        server_ver = version_info.get("Server", {}).get("Version", "Unknown")
        print(f"Docker Client: {client_ver}")
        print(f"Docker Server: {server_ver}")
    else:
        print(f"Docker Version: ERROR - {version_info.get('error')}")
    print()
    
    # BuildKit
    buildkit = diagnostics.get("buildkit", {})
    print(f"BuildKit Version: {buildkit.get('buildkit_version', 'Unknown')}")
    print(f"BuildKit Default: {'Yes' if buildkit.get('enabled_by_default') else 'No'}")
    print()
    
    # Compose
    compose = diagnostics.get("compose", {})
    if "error" not in compose:
        print(f"Compose Version: {compose.get('version', 'Unknown')}")
        print(f"Compose Command: {compose.get('command', 'Unknown')}")
        if compose.get("warning"):
            print(f"⚠️  WARNING: {compose['warning']}")
    else:
        print(f"Compose: ERROR - {compose.get('error')}")
    print()
    
    # Containers
    running = diagnostics.get("running_containers", [])
    all_containers = diagnostics.get("all_containers", [])
    print(f"Running Containers: {len(running)}")
    print(f"Total Containers: {len(all_containers)}")
    for c in running:
        print(f"  - {c.get('name', 'unnamed')}: {c.get('image', 'unknown')} ({c.get('status', '')})")
    print()
    
    # Images
    images = diagnostics.get("images", [])
    print(f"Images: {len(images)}")
    print()
    
    # Compose File
    compose_file = diagnostics.get("compose_file", {})
    if compose_file.get("found"):
        print(f"Compose File: {compose_file.get('file')}")
        print(f"Services: {', '.join(compose_file.get('services', []))}")
        if compose_file.get("warning"):
            print(f"⚠️  WARNING: {compose_file['warning']}")
    else:
        print("Compose File: Not found in current directory")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    diagnostics = run_full_diagnostics()
    
    if "--json" in sys.argv:
        print(json.dumps(diagnostics, indent=2))
    else:
        print_summary(diagnostics)
