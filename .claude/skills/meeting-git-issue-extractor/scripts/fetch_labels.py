#!/usr/bin/env python3
"""
Fetch available GitHub labels for the repository.

Usage:
    python fetch_labels.py [--format json|table|simple]

Example:
    python fetch_labels.py
    python fetch_labels.py --format json
"""

import argparse
import json
import subprocess
import sys


def fetch_labels(output_format: str = "table") -> list:
    """Fetch labels from GitHub using gh CLI."""

    try:
        result = subprocess.run(
            ["gh", "label", "list", "--json", "name,description,color"],
            capture_output=True,
            text=True,
            check=True
        )
        labels = json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error fetching labels: {e.stderr}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("❌ Error parsing label data")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ gh CLI not found. Please install GitHub CLI.")
        sys.exit(1)

    if output_format == "json":
        print(json.dumps(labels, indent=2))
    elif output_format == "simple":
        for label in labels:
            print(label["name"])
    else:  # table format
        print("\n📋 Available GitHub Labels\n")
        print(f"{'Label Name':<30} {'Description':<50}")
        print("-" * 80)
        for label in sorted(labels, key=lambda x: x["name"]):
            name = label["name"]
            desc = label.get("description", "") or "(no description)"
            # Truncate description if too long
            if len(desc) > 47:
                desc = desc[:47] + "..."
            print(f"{name:<30} {desc:<50}")
        print(f"\nTotal: {len(labels)} labels")

    return labels


def get_label_suggestions(topic: str, labels: list) -> list:
    """Suggest labels based on topic keywords."""

    suggestions = []
    topic_lower = topic.lower()

    # Keyword mappings
    keywords = {
        "bug": ["bug", "fix"],
        "feature": ["feature", "add", "new", "implement"],
        "enhancement": ["enhancement", "improve", "update", "refactor"],
        "ui": ["ui", "frontend", "template", "css", "design"],
        "backend": ["backend", "api", "model", "view", "service"],
        "documentation": ["doc", "readme", "guide"],
        "testing": ["test", "qa", "playwright"],
    }

    for label in labels:
        label_name = label["name"].lower()
        label_desc = (label.get("description") or "").lower()

        # Check if any keyword matches
        for category, kw_list in keywords.items():
            if any(kw in topic_lower for kw in kw_list):
                if category in label_name or category in label_desc:
                    suggestions.append(label["name"])
                    break

    return list(set(suggestions))


def main():
    parser = argparse.ArgumentParser(
        description="Fetch available GitHub labels"
    )
    parser.add_argument(
        "--format",
        choices=["json", "table", "simple"],
        default="table",
        help="Output format (default: table)"
    )
    parser.add_argument(
        "--suggest",
        help="Suggest labels for a topic"
    )

    args = parser.parse_args()

    labels = fetch_labels(args.format)

    if args.suggest:
        suggestions = get_label_suggestions(args.suggest, labels)
        if suggestions:
            print(f"\n💡 Suggested labels for '{args.suggest}':")
            for label in suggestions:
                print(f"  - {label}")
        else:
            print(f"\nNo specific suggestions for '{args.suggest}'")


if __name__ == "__main__":
    main()
