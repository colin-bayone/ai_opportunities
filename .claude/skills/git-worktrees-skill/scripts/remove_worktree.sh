#!/bin/bash
#
# remove_worktree.sh - Safely remove a git worktree (directory only)
#
# Usage: ./remove_worktree.sh <name> [-y|--yes]
#
# This script ONLY removes the worktree directory. It does NOT delete branches.
# Branch cleanup must be done manually by the user if desired.
#
# Examples:
#   ./remove_worktree.sh feature-name       # Interactive (asks for confirmation)
#   ./remove_worktree.sh pr-review --yes    # Non-interactive (skips confirmation)

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

show_help() {
    echo "Usage: $0 <name> [OPTIONS]"
    echo ""
    echo "Safely remove a git worktree directory."
    echo ""
    echo "Arguments:"
    echo "  <name>              Worktree name (e.g., 'pr-568' for talent_ai-pr-568)"
    echo ""
    echo "Options:"
    echo "  -y, --yes           Skip confirmation (REQUIRES EXPLICIT USER APPROVAL FIRST)"
    echo "  -h, --help          Show this help message"
    echo ""
    echo "Safety checks (always run, even with --yes):"
    echo "  - Warns if uncommitted changes exist"
    echo "  - Warns if unpushed commits exist"
    echo ""
    echo "IMPORTANT - Confirmation requirement:"
    echo "  This script requires interactive confirmation before removal."
    echo "  This is a SAFETY FEATURE to prevent accidental data loss."
    echo ""
    echo "  DO NOT use --yes unless the user has EXPLICITLY confirmed they want"
    echo "  the worktree removed. Always ask the user first."
    echo ""
    echo "  The --yes flag should ONLY be SUGGESTED when:"
    echo "    - You have already reviewed the worktree status"
    echo "    - You have confirmed there are no uncommitted/unpushed changes"
    echo "    - The user explicitly approves the removal"
    echo ""
    echo "Examples:"
    echo "  $0 pr-568           # Interactive: asks for confirmation (DEFAULT)"
    echo "  $0 pr-568 --yes     # ONLY after user explicitly confirms removal"
    echo ""
    echo "Note: This script ONLY removes the worktree directory."
    echo "      The branch will NOT be deleted. Delete manually if desired:"
    echo "        git branch -d <branch-name>    # Safe delete (only if merged)"
    echo "        git branch -D <branch-name>    # Force delete"
}

# Get script directory and repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
REPO_NAME="$(basename "$REPO_ROOT")"
PARENT_DIR="$(dirname "$REPO_ROOT")"

# Parse arguments
WORKTREE_NAME=""
SKIP_CONFIRM=true

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -y|--yes)
            SKIP_CONFIRM=true
            shift
            ;;
        -*)
            echo -e "${RED}Error: Unknown option '$1'${NC}"
            echo ""
            echo "Run '$0 --help' for usage information."
            exit 1
            ;;
        *)
            if [[ -z "$WORKTREE_NAME" ]]; then
                WORKTREE_NAME="$1"
            else
                echo -e "${RED}Error: Unexpected argument '$1'${NC}"
                echo ""
                echo "Run '$0 --help' for usage information."
                exit 1
            fi
            shift
            ;;
    esac
done

# Validate inputs
if [[ -z "$WORKTREE_NAME" ]]; then
    echo -e "${RED}Error: Worktree name is required${NC}"
    echo "Usage: $0 <name>"
    echo ""
    echo "Current worktrees:"
    git -C "$REPO_ROOT" worktree list
    exit 1
fi

# Construct path
WORKTREE_DIR="$PARENT_DIR/${REPO_NAME}-${WORKTREE_NAME}"

cd "$REPO_ROOT"

# Check if worktree exists
if [[ ! -d "$WORKTREE_DIR" ]]; then
    # Try to find by exact path match in worktree list
    FOUND_PATH=$(git worktree list --porcelain | grep "^worktree" | grep -F "$WORKTREE_NAME" | head -1 | sed 's/^worktree //')

    if [[ -n "$FOUND_PATH" && -d "$FOUND_PATH" ]]; then
        WORKTREE_DIR="$FOUND_PATH"
    else
        echo -e "${RED}Error: Worktree not found: $WORKTREE_DIR${NC}"
        echo ""
        echo "Available worktrees:"
        git worktree list
        exit 1
    fi
fi

# Prevent removing main worktree
if [[ "$WORKTREE_DIR" == "$REPO_ROOT" ]]; then
    echo -e "${RED}Error: Cannot remove the main worktree${NC}"
    exit 1
fi

# Get branch name for this worktree
BRANCH_NAME=$(git worktree list --porcelain | grep -A2 "^worktree $WORKTREE_DIR$" | grep "^branch" | sed 's/^branch refs\/heads\///')

echo -e "${BLUE}Worktree Removal${NC}"
echo "================"
echo ""
echo "  Path: $WORKTREE_DIR"
echo "  Branch: $BRANCH_NAME"
echo ""

# Safety checks
cd "$WORKTREE_DIR"

# Check for uncommitted changes
CHANGES=$(git status --porcelain 2>/dev/null | wc -l)
if [[ $CHANGES -gt 0 ]]; then
    echo -e "${RED}WARNING: Found $CHANGES uncommitted changes:${NC}"
    git status --short
    echo ""
fi

# Check for unpushed commits
if [[ -n "$BRANCH_NAME" ]]; then
    # Check if remote branch exists
    if git show-ref --verify --quiet "refs/remotes/origin/${BRANCH_NAME}" 2>/dev/null; then
        UNPUSHED=$(git log "origin/${BRANCH_NAME}..HEAD" --oneline 2>/dev/null | wc -l)
        if [[ $UNPUSHED -gt 0 ]]; then
            echo -e "${YELLOW}WARNING: Found $UNPUSHED unpushed commit(s):${NC}"
            git log "origin/${BRANCH_NAME}..HEAD" --oneline 2>/dev/null
            echo ""
        fi
    else
        # Branch doesn't exist on remote at all
        LOCAL_COMMITS=$(git log --oneline 2>/dev/null | wc -l)
        echo -e "${YELLOW}NOTE: Branch '$BRANCH_NAME' has not been pushed to remote.${NC}"
        echo ""
    fi
fi

cd "$REPO_ROOT"

# Confirmation
echo -e "${YELLOW}This will remove the worktree directory only.${NC}"
echo "The branch '$BRANCH_NAME' will NOT be deleted."
echo ""

if [[ ! -t 0 ]]; then
    # Not running in interactive terminal - require explicit --yes flag
    if [[ "$SKIP_CONFIRM" == "true" ]]; then
        echo -e "${YELLOW}WARNING: Proceeding without interactive confirmation (--yes flag).${NC}"
        echo ""
    else
        echo -e "${YELLOW}════════════════════════════════════════════════════════════════${NC}"
        echo -e "${YELLOW}  CONFIRMATION REQUIRED${NC}"
        echo -e "${YELLOW}════════════════════════════════════════════════════════════════${NC}"
        echo ""
        echo "This script requires interactive confirmation before removing a worktree."
        echo "You are running in a non-interactive terminal (e.g., from automation)."
        echo ""
        echo -e "${BLUE}Options:${NC}"
        echo ""
        echo "  1. Run this command manually in your terminal:"
        echo "     $0 $WORKTREE_NAME"
        echo ""
        echo "  2. If you've reviewed the worktree and confirm removal, re-run with --yes:"
        echo "     $0 $WORKTREE_NAME --yes"
        echo ""
        echo "  3. Use git directly (bypasses this script's safety checks):"
        echo "     git worktree remove $WORKTREE_DIR"
        echo ""
        echo -e "${RED}The --yes flag should only be used after you have reviewed the worktree${NC}"
        echo -e "${RED}and confirmed there are no uncommitted changes or unpushed commits.${NC}"
        exit 1
    fi
else
    # Interactive terminal - ask for confirmation
    read -p "Remove worktree at $WORKTREE_DIR? (y/N) " -n 1 -r
    echo

    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled."
        exit 0
    fi
fi

# Remove the worktree
echo ""
echo -e "${BLUE}Removing worktree directory...${NC}"
git worktree remove "$WORKTREE_DIR"

# Clean up any stale worktree references
git worktree prune

echo -e "${GREEN}Worktree removed successfully!${NC}"
echo ""
echo "The branch '$BRANCH_NAME' still exists."
echo "To delete the branch manually (if desired):"
echo "  git branch -d $BRANCH_NAME    # Safe delete (only if merged)"
echo "  git branch -D $BRANCH_NAME    # Force delete"
echo ""
echo "Remaining worktrees:"
git worktree list
