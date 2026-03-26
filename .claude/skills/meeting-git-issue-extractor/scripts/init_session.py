#!/usr/bin/env python3
"""
Initialize a new meeting-git-issue-extractor session folder.

Usage:
    python init_session.py <topic-slug> [--path <base-path>]

Example:
    python init_session.py pallavi-ui-call
    python init_session.py pallavi-ui-call --path /custom/path
"""

import argparse
import json
import os
import sys
import uuid
from datetime import datetime
from pathlib import Path


def create_session_folder(topic_slug: str, base_path: str = None) -> Path:
    """Create the session folder structure for a new extraction session."""

    # Determine base path
    if base_path:
        base = Path(base_path)
    else:
        # Default to project root / claude /
        script_dir = Path(__file__).parent
        project_root = script_dir.parent.parent.parent.parent  # Up from scripts/ -> skill/ -> skills/ -> .claude/ -> project
        base = project_root / "claude"

    # Create dated folder name
    date_str = datetime.now().strftime("%Y-%m-%d")
    folder_name = f"{date_str}_{topic_slug}"
    session_path = base / folder_name

    # Check if folder already exists
    if session_path.exists():
        print(f"⚠️  Session folder already exists: {session_path}")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)

    # Create folder structure
    folders = [
        "orchestration",
        "agents/document-analyzer",
        "agents/codebase-explorer",
        "agents/issue-drafter",
        "agents/issue-reviewer",
        "research",
        "issues",
        "issues/attachments",
        "decisions",
        "source",
    ]

    for folder in folders:
        (session_path / folder).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {folder}/")

    # Create initial state.json
    state = {
        "session_id": str(uuid.uuid4()),
        "created_at": datetime.now().isoformat(),
        "topic_slug": topic_slug,
        "current_phase": "setup",
        "completed_phases": [],
        "workflow_mode": None,
        "topics": [],
        "issues_created": [],
        "pending_approvals": [],
        "last_activity": datetime.now().isoformat(),
    }

    state_file = session_path / "orchestration" / "state.json"
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)
    print(f"✅ Created: orchestration/state.json")

    # Create placeholder files
    placeholders = {
        "orchestration/00_master_plan.md": "# Master Plan\n\n*To be populated during analysis phase*\n",
        "orchestration/01_topic_breakdown.md": "# Topic Breakdown\n\n*To be populated during analysis phase*\n",
        "orchestration/02_agent_assignments.md": "# Agent Assignments\n\n*To be populated during exploration phase*\n",
        "decisions/clarifications.md": "# Clarification Q&A Log\n\n*Questions and user decisions will be logged here*\n",
        "issues/attachments/README.md": """# Issue Attachments

This folder contains screenshots and images for GitHub issues.

## Structure

```
attachments/
├── 01_issue-name/
│   ├── screenshot1.png
│   └── mockup.png
├── 02_another-issue/
│   └── diagram.png
└── README.md
```

## Capturing Screenshots (Playwright)

Use the Phoenix Theme skill's Playwright integration for automated screenshots:

```bash
# Ensure dev server is running and DEV_AUTH_ENABLED=True in .env.local

# Take authenticated screenshot
poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py \\
    --url http://localhost:8000/candidates/search/ \\
    --email user@bayone.com \\
    --output issues/attachments/01_issue-name/screenshot.png
```

See `docs/playwright-testing-guide.md` and PR #820 for full details.

## Uploading to GitHub Issues

The `gh` CLI does not support uploading attachments directly. Use one of these methods:

### Option A: Web Upload (Recommended)
```bash
# Open the issue in browser
gh issue view <number> --web
```
Then drag/drop images from this folder into the comment box.

### Option B: Create with --web flag
```bash
gh issue create --title "..." --body-file ... --web
```
This opens browser where you can attach files before submitting.

### Option C: Add as comment
1. Create issue via CLI
2. Open in browser: `gh issue view <number> --web`
3. Add comment with attached images

## Private Repository Security

- Attachments are stored on GitHub's CDN
- Only users with repo access can view them
- Links have token expiration for security
""",
    }

    for file_path, content in placeholders.items():
        file = session_path / file_path
        with open(file, 'w') as f:
            f.write(content)
        print(f"✅ Created: {file_path}")

    print(f"\n🎉 Session folder created: {session_path}")
    print(f"\nNext steps:")
    print(f"  1. Add source documents to: {session_path}/source/")
    print(f"  2. Run the meeting-git-issue-extractor skill")

    return session_path


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new meeting-git-issue-extractor session"
    )
    parser.add_argument(
        "topic_slug",
        help="Topic slug for the session (e.g., 'pallavi-ui-call')"
    )
    parser.add_argument(
        "--path",
        help="Base path for claude/ folder (defaults to project root)"
    )

    args = parser.parse_args()

    # Validate topic slug
    if not args.topic_slug.replace("-", "").replace("_", "").isalnum():
        print("❌ Topic slug should only contain letters, numbers, hyphens, and underscores")
        sys.exit(1)

    create_session_folder(args.topic_slug, args.path)


if __name__ == "__main__":
    main()
