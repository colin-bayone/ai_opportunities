#!/usr/bin/env python3
"""
Check that required pip dependencies are installed.
Exits 0 if all present, exits 1 with clear instructions if any missing.
"""

import sys

REQUIRED = {
    "requests": "requests",
    "msal": "msal",
    "dotenv": "python-dotenv",
}

missing = []

for import_name, pip_name in REQUIRED.items():
    try:
        __import__(import_name)
    except ImportError:
        missing.append(pip_name)

if missing:
    print(f"ERROR: Missing required packages: {', '.join(missing)}")
    print(f"Install with: pip install {' '.join(missing)}")
    print(f"Or: pip install -r .claude/skills/fido/scripts/requirements.txt")
    sys.exit(1)

print("All dependencies installed.")
sys.exit(0)
