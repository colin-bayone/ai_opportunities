#!/bin/bash
#
# list_worktrees.sh - List all git worktrees with status information
#
# Usage: ./list_worktrees.sh [options]
#
# Options:
#   --verbose    Show detailed info (commits behind, uncommitted changes)
#   --json       Output as JSON for scripting

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Get script directory and repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

# Parse arguments
VERBOSE=false
JSON_OUTPUT=false
while [[ $# -gt 0 ]]; do
    case $1 in
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --json)
            JSON_OUTPUT=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  --verbose, -v    Show detailed info"
            echo "  --json           Output as JSON"
            exit 0
            ;;
        *)
            echo -e "${RED}Error: Unknown option $1${NC}"
            exit 1
            ;;
    esac
done

cd "$REPO_ROOT"

# Fetch to ensure we have latest remote info (suppress errors if offline)
git fetch origin --quiet 2>/dev/null || true

# Get main branch name
MAIN_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || echo "main")

# JSON output
if [[ "$JSON_OUTPUT" == true ]]; then
    echo "["
    FIRST=true
    JSON_COUNT=0

    while IFS= read -r line || [[ -n "$line" ]]; do
        if [[ $line == worktree* ]]; then
            WORKTREE_PATH="${line#worktree }"
        elif [[ $line == HEAD* ]]; then
            COMMIT="${line#HEAD }"
        elif [[ $line == branch* ]]; then
            BRANCH="${line#branch refs/heads/}"
        elif [[ $line == detached ]]; then
            BRANCH="(detached)"
        elif [[ -z $line ]]; then
            # End of worktree entry, output JSON
            if [[ -n "$WORKTREE_PATH" ]]; then
                # Get status info
                DIRTY="false"
                AHEAD=0
                BEHIND=0

                if [[ -d "$WORKTREE_PATH" ]]; then
                    cd "$WORKTREE_PATH"

                    # Check for uncommitted changes
                    if [[ -n $(git status --porcelain 2>/dev/null) ]]; then
                        DIRTY="true"
                    fi

                    # Get ahead/behind counts
                    if [[ "$BRANCH" != "(detached)" ]]; then
                        COUNTS=$(git rev-list --left-right --count "origin/${MAIN_BRANCH}...HEAD" 2>/dev/null || echo "0 0")
                        BEHIND=$(echo "$COUNTS" | awk '{print $1}')
                        AHEAD=$(echo "$COUNTS" | awk '{print $2}')
                    fi

                    cd "$REPO_ROOT"
                fi

                [[ "$FIRST" == true ]] || echo ","
                FIRST=false
                JSON_COUNT=$((JSON_COUNT + 1))

                echo "  {"
                echo "    \"path\": \"$WORKTREE_PATH\","
                echo "    \"branch\": \"$BRANCH\","
                echo "    \"commit\": \"${COMMIT:0:8}\","
                echo "    \"dirty\": $DIRTY,"
                echo "    \"ahead\": $AHEAD,"
                echo "    \"behind\": $BEHIND"
                echo -n "  }"
            fi

            WORKTREE_PATH=""
            COMMIT=""
            BRANCH=""
        fi
    done < <(git worktree list --porcelain; echo "")

    echo ""
    echo "]"
    exit 0
fi

# Human-readable output
echo -e "${BLUE}Git Worktrees${NC}"
echo "============="
echo ""

WORKTREE_COUNT=0

while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ $line == worktree* ]]; then
        WORKTREE_PATH="${line#worktree }"
    elif [[ $line == HEAD* ]]; then
        COMMIT="${line#HEAD }"
    elif [[ $line == branch* ]]; then
        BRANCH="${line#branch refs/heads/}"
    elif [[ $line == detached ]]; then
        BRANCH="(detached HEAD)"
    elif [[ -z $line ]]; then
        # End of worktree entry, display it
        if [[ -n "$WORKTREE_PATH" ]]; then
            WORKTREE_COUNT=$((WORKTREE_COUNT + 1))

            # Determine if this is main worktree
            if [[ "$WORKTREE_PATH" == "$REPO_ROOT" ]]; then
                LABEL="${CYAN}[main worktree]${NC}"
            else
                LABEL=""
            fi

            echo -e "${GREEN}$WORKTREE_PATH${NC} $LABEL"
            echo -e "  Branch: ${YELLOW}$BRANCH${NC}"
            echo -e "  Commit: ${COMMIT:0:8}"

            if [[ "$VERBOSE" == true && -d "$WORKTREE_PATH" ]]; then
                cd "$WORKTREE_PATH"

                # Check for uncommitted changes
                CHANGES=$(git status --porcelain 2>/dev/null | wc -l)
                if [[ $CHANGES -gt 0 ]]; then
                    echo -e "  Status: ${RED}$CHANGES uncommitted changes${NC}"
                else
                    echo -e "  Status: ${GREEN}Clean${NC}"
                fi

                # Get ahead/behind counts relative to main
                if [[ "$BRANCH" != "(detached HEAD)" ]]; then
                    COUNTS=$(git rev-list --left-right --count "origin/${MAIN_BRANCH}...HEAD" 2>/dev/null || echo "0 0")
                    BEHIND=$(echo "$COUNTS" | awk '{print $1}')
                    AHEAD=$(echo "$COUNTS" | awk '{print $2}')

                    if [[ $AHEAD -gt 0 || $BEHIND -gt 0 ]]; then
                        STATUS=""
                        [[ $AHEAD -gt 0 ]] && STATUS="${GREEN}$AHEAD ahead${NC}"
                        [[ $AHEAD -gt 0 && $BEHIND -gt 0 ]] && STATUS="$STATUS, "
                        [[ $BEHIND -gt 0 ]] && STATUS="${STATUS}${YELLOW}$BEHIND behind${NC}"
                        echo -e "  vs $MAIN_BRANCH: $STATUS"
                    fi
                fi

                cd "$REPO_ROOT"
            fi

            echo ""
        fi

        WORKTREE_PATH=""
        COMMIT=""
        BRANCH=""
    fi
done < <(git worktree list --porcelain; echo "")

# Handle zero worktrees case (shouldn't happen - main repo is always a worktree)
if [[ $WORKTREE_COUNT -eq 0 ]]; then
    echo -e "${YELLOW}No worktrees found.${NC}"
    echo ""
    echo "This is unexpected - your main repository should always appear as a worktree."
    echo "Try running: git worktree list"
else
    echo -e "Total: ${BLUE}$WORKTREE_COUNT${NC} worktree(s)"

    if [[ $WORKTREE_COUNT -eq 1 ]]; then
        echo ""
        echo "You have only your main repository. Create additional worktrees with:"
        echo "  .claude/skills/git-worktrees-skill/scripts/create_worktree.sh <name>"
    fi
fi

if [[ "$VERBOSE" == false && $WORKTREE_COUNT -gt 0 ]]; then
    echo ""
    echo "Use --verbose for more details"
fi
