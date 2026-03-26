#!/bin/bash
#
# create_worktree.sh - Create a new git worktree with environment setup
#
# Usage: ./create_worktree.sh <name> [options]
#
# Options:
#   --base <branch>   Base branch for new worktree (default: current branch)
#   --pr <number>     Fetch and checkout a PR branch instead of creating new
#   --no-setup        Skip environment setup (poetry install, etc.)
#   --path <dir>      Custom parent directory (default: parent of repo)
#
# Examples:
#   ./create_worktree.sh new-feature
#   ./create_worktree.sh pr-review --pr 445
#   ./create_worktree.sh hotfix --base main

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory and repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
REPO_NAME="$(basename "$REPO_ROOT")"

# Default values
BASE_BRANCH=""
PR_NUMBER=""
DO_SETUP=true
PARENT_DIR="$(dirname "$REPO_ROOT")"

# Parse arguments
WORKTREE_NAME=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --base)
            BASE_BRANCH="$2"
            shift 2
            ;;
        --pr)
            PR_NUMBER="$2"
            shift 2
            ;;
        --no-setup)
            DO_SETUP=false
            shift
            ;;
        --path)
            PARENT_DIR="$2"
            shift 2
            ;;
        -h|--help)
            echo "Usage: $0 <name> [options]"
            echo ""
            echo "Options:"
            echo "  --base <branch>   Base branch for new worktree (default: current branch)"
            echo "  --pr <number>     Fetch and checkout a PR branch"
            echo "  --no-setup        Skip environment setup"
            echo "  --path <dir>      Custom parent directory"
            exit 0
            ;;
        -*)
            echo -e "${RED}Error: Unknown option $1${NC}"
            exit 1
            ;;
        *)
            if [[ -z "$WORKTREE_NAME" ]]; then
                WORKTREE_NAME="$1"
            else
                echo -e "${RED}Error: Unexpected argument $1${NC}"
                exit 1
            fi
            shift
            ;;
    esac
done

# Validate inputs
if [[ -z "$WORKTREE_NAME" ]]; then
    echo -e "${RED}Error: Worktree name is required${NC}"
    echo "Usage: $0 <name> [options]"
    exit 1
fi

# Construct paths
WORKTREE_DIR="$PARENT_DIR/${REPO_NAME}-${WORKTREE_NAME}"
BRANCH_NAME="$WORKTREE_NAME"

echo -e "${BLUE}Creating worktree: ${WORKTREE_NAME}${NC}"
echo "  Repository: $REPO_ROOT"
echo "  Worktree path: $WORKTREE_DIR"

# Check if worktree already exists
if [[ -d "$WORKTREE_DIR" ]]; then
    echo -e "${RED}Error: Directory already exists: $WORKTREE_DIR${NC}"
    echo "Use a different name or remove the existing directory first."
    exit 1
fi

# Change to repo root
cd "$REPO_ROOT"

# Handle PR checkout
if [[ -n "$PR_NUMBER" ]]; then
    echo -e "${BLUE}Fetching PR #${PR_NUMBER}...${NC}"

    # Get PR branch name
    PR_BRANCH=$(gh pr view "$PR_NUMBER" --json headRefName -q '.headRefName' 2>/dev/null)
    if [[ -z "$PR_BRANCH" ]]; then
        echo -e "${RED}Error: Could not find PR #${PR_NUMBER}${NC}"
        exit 1
    fi

    echo "  PR branch: $PR_BRANCH"

    # Fetch the PR
    git fetch origin "pull/${PR_NUMBER}/head:${PR_BRANCH}" 2>/dev/null || \
        git fetch origin "$PR_BRANCH" 2>/dev/null || true

    BRANCH_NAME="$PR_BRANCH"

    # Check if branch is already checked out
    EXISTING=$(git worktree list --porcelain | grep -A1 "worktree" | grep "branch refs/heads/${BRANCH_NAME}" || true)
    if [[ -n "$EXISTING" ]]; then
        echo -e "${RED}Error: Branch '$BRANCH_NAME' is already checked out in another worktree${NC}"
        git worktree list
        exit 1
    fi

    # Create worktree with existing branch
    echo -e "${BLUE}Creating worktree...${NC}"
    git worktree add "$WORKTREE_DIR" "$BRANCH_NAME"

else
    # Create new branch from base
    if [[ -z "$BASE_BRANCH" ]]; then
        BASE_BRANCH=$(git rev-parse --abbrev-ref HEAD)
    fi

    echo "  Base branch: $BASE_BRANCH"
    echo "  New branch: $BRANCH_NAME"

    # Fetch latest
    echo -e "${BLUE}Fetching latest...${NC}"
    git fetch origin "$BASE_BRANCH" 2>/dev/null || true

    # Check if branch already exists
    if git show-ref --verify --quiet "refs/heads/${BRANCH_NAME}"; then
        echo -e "${YELLOW}Warning: Branch '$BRANCH_NAME' already exists${NC}"

        # Check if it's checked out elsewhere
        EXISTING=$(git worktree list --porcelain | grep -A1 "worktree" | grep "branch refs/heads/${BRANCH_NAME}" || true)
        if [[ -n "$EXISTING" ]]; then
            echo -e "${RED}Error: Branch is already checked out in another worktree${NC}"
            git worktree list
            exit 1
        fi

        # Use existing branch
        echo -e "${BLUE}Creating worktree with existing branch...${NC}"
        git worktree add "$WORKTREE_DIR" "$BRANCH_NAME"
    else
        # Create new branch
        echo -e "${BLUE}Creating worktree with new branch...${NC}"
        git worktree add -b "$BRANCH_NAME" "$WORKTREE_DIR" "origin/${BASE_BRANCH}" 2>/dev/null || \
            git worktree add -b "$BRANCH_NAME" "$WORKTREE_DIR" "$BASE_BRANCH"
    fi
fi

echo -e "${GREEN}Worktree created successfully!${NC}"

# Environment setup
if [[ "$DO_SETUP" == true ]]; then
    echo ""
    echo -e "${BLUE}Setting up environment...${NC}"

    cd "$WORKTREE_DIR"

    # Copy environment files if they exist
    if [[ -f "$REPO_ROOT/.env.local" ]]; then
        echo "  Copying .env.local..."
        cp "$REPO_ROOT/.env.local" "$WORKTREE_DIR/.env.local"
    fi

    # Python/Poetry setup
    if [[ -f "pyproject.toml" ]]; then
        echo "  Installing Python dependencies (poetry)..."
        poetry install --no-root 2>&1 | tail -5
    elif [[ -f "requirements.txt" ]]; then
        echo "  Installing Python dependencies (pip)..."
        pip install -r requirements.txt 2>&1 | tail -5
    fi

    # Node.js setup
    if [[ -f "package.json" ]]; then
        if [[ -f "yarn.lock" ]]; then
            echo "  Installing Node dependencies (yarn)..."
            yarn install 2>&1 | tail -5
        elif [[ -f "package-lock.json" ]] || [[ -f "npm-shrinkwrap.json" ]]; then
            echo "  Installing Node dependencies (npm)..."
            npm ci 2>&1 | tail -5
        else
            echo "  Installing Node dependencies (npm install)..."
            npm install 2>&1 | tail -5
        fi
    fi

    echo -e "${GREEN}Environment setup complete!${NC}"
fi

# Summary
echo ""
echo -e "${GREEN}=== Worktree Ready ===${NC}"
echo ""
echo "  Location: $WORKTREE_DIR"
echo "  Branch: $BRANCH_NAME"
echo ""
echo "To start working:"
echo -e "  ${YELLOW}cd $WORKTREE_DIR${NC}"
echo -e "  ${YELLOW}claude${NC}"
echo ""
echo "To remove later:"
echo -e "  ${YELLOW}.claude/skills/git-worktrees-skill/scripts/remove_worktree.sh $WORKTREE_NAME${NC}"
