#!/bin/bash
#
# setup_env.sh - Set up development environment in a worktree
#
# Usage: ./setup_env.sh [options]
#
# Options:
#   --skip-deps    Skip dependency installation
#   --migrate      Run Django migrations after setup
#   --copy-env     Copy .env files from main worktree
#
# This script auto-detects and sets up:
#   - Python (Poetry, pip, requirements.txt)
#   - Node.js (npm, yarn, pnpm)
#   - Environment files

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get current directory
WORKTREE_DIR="$(pwd)"

# Try to find main worktree
MAIN_WORKTREE=$(git worktree list --porcelain | head -1 | sed 's/^worktree //')

# Default values
SKIP_DEPS=false
RUN_MIGRATE=false
COPY_ENV=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-deps)
            SKIP_DEPS=true
            shift
            ;;
        --migrate)
            RUN_MIGRATE=true
            shift
            ;;
        --copy-env)
            COPY_ENV=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  --skip-deps    Skip dependency installation"
            echo "  --migrate      Run Django migrations after setup"
            echo "  --copy-env     Copy .env files from main worktree"
            exit 0
            ;;
        *)
            echo -e "${RED}Error: Unknown option $1${NC}"
            exit 1
            ;;
    esac
done

echo -e "${BLUE}Setting up environment in: $WORKTREE_DIR${NC}"
echo ""

# Copy environment files if requested
if [[ "$COPY_ENV" == true && -n "$MAIN_WORKTREE" && "$MAIN_WORKTREE" != "$WORKTREE_DIR" ]]; then
    echo -e "${BLUE}Copying environment files from main worktree...${NC}"

    for env_file in .env .env.local .env.development .env.dev; do
        if [[ -f "$MAIN_WORKTREE/$env_file" && ! -f "$WORKTREE_DIR/$env_file" ]]; then
            echo "  Copying $env_file"
            cp "$MAIN_WORKTREE/$env_file" "$WORKTREE_DIR/$env_file"
        fi
    done
    echo ""
fi

# Skip dependency installation if requested
if [[ "$SKIP_DEPS" == true ]]; then
    echo -e "${YELLOW}Skipping dependency installation (--skip-deps)${NC}"
else
    # Python setup
    if [[ -f "pyproject.toml" ]]; then
        # Check if Poetry is available
        if command -v poetry &> /dev/null; then
            echo -e "${BLUE}Installing Python dependencies (Poetry)...${NC}"
            poetry install --no-root
            echo -e "${GREEN}Poetry dependencies installed!${NC}"
        else
            echo -e "${YELLOW}Warning: pyproject.toml found but Poetry not available${NC}"

            # Try pip if requirements.txt exists
            if [[ -f "requirements.txt" ]]; then
                echo -e "${BLUE}Falling back to pip...${NC}"
                pip install -r requirements.txt
            fi
        fi
        echo ""
    elif [[ -f "requirements.txt" ]]; then
        echo -e "${BLUE}Installing Python dependencies (pip)...${NC}"
        pip install -r requirements.txt
        echo -e "${GREEN}Pip dependencies installed!${NC}"
        echo ""
    elif [[ -f "setup.py" ]]; then
        echo -e "${BLUE}Installing Python package (setup.py)...${NC}"
        pip install -e .
        echo -e "${GREEN}Package installed!${NC}"
        echo ""
    fi

    # Node.js setup
    if [[ -f "package.json" ]]; then
        if [[ -f "pnpm-lock.yaml" ]]; then
            if command -v pnpm &> /dev/null; then
                echo -e "${BLUE}Installing Node dependencies (pnpm)...${NC}"
                pnpm install
                echo -e "${GREEN}pnpm dependencies installed!${NC}"
            else
                echo -e "${YELLOW}Warning: pnpm-lock.yaml found but pnpm not available${NC}"
            fi
        elif [[ -f "yarn.lock" ]]; then
            if command -v yarn &> /dev/null; then
                echo -e "${BLUE}Installing Node dependencies (yarn)...${NC}"
                yarn install
                echo -e "${GREEN}Yarn dependencies installed!${NC}"
            else
                echo -e "${YELLOW}Warning: yarn.lock found but yarn not available${NC}"
            fi
        elif [[ -f "package-lock.json" ]]; then
            if command -v npm &> /dev/null; then
                echo -e "${BLUE}Installing Node dependencies (npm ci)...${NC}"
                npm ci
                echo -e "${GREEN}npm dependencies installed!${NC}"
            else
                echo -e "${YELLOW}Warning: package-lock.json found but npm not available${NC}"
            fi
        else
            if command -v npm &> /dev/null; then
                echo -e "${BLUE}Installing Node dependencies (npm install)...${NC}"
                npm install
                echo -e "${GREEN}npm dependencies installed!${NC}"
            else
                echo -e "${YELLOW}Warning: package.json found but npm not available${NC}"
            fi
        fi
        echo ""
    fi

    # Ruby setup
    if [[ -f "Gemfile" ]]; then
        if command -v bundle &> /dev/null; then
            echo -e "${BLUE}Installing Ruby dependencies (bundler)...${NC}"
            bundle install
            echo -e "${GREEN}Bundler dependencies installed!${NC}"
        else
            echo -e "${YELLOW}Warning: Gemfile found but bundler not available${NC}"
        fi
        echo ""
    fi

    # Go setup
    if [[ -f "go.mod" ]]; then
        if command -v go &> /dev/null; then
            echo -e "${BLUE}Installing Go dependencies...${NC}"
            go mod download
            echo -e "${GREEN}Go dependencies installed!${NC}"
        else
            echo -e "${YELLOW}Warning: go.mod found but go not available${NC}"
        fi
        echo ""
    fi

    # Rust setup
    if [[ -f "Cargo.toml" ]]; then
        if command -v cargo &> /dev/null; then
            echo -e "${BLUE}Building Rust project...${NC}"
            cargo build
            echo -e "${GREEN}Rust project built!${NC}"
        else
            echo -e "${YELLOW}Warning: Cargo.toml found but cargo not available${NC}"
        fi
        echo ""
    fi
fi

# Django migrations
if [[ "$RUN_MIGRATE" == true ]]; then
    if [[ -f "manage.py" ]]; then
        echo -e "${BLUE}Running Django migrations...${NC}"

        # Try to determine the environment
        if [[ -n "$DJANGO_ENVIRONMENT" ]]; then
            DJANGO_ENV="$DJANGO_ENVIRONMENT"
        elif [[ -f ".env.local" ]]; then
            DJANGO_ENV="local"
        else
            DJANGO_ENV="local"
        fi

        DJANGO_ENVIRONMENT=$DJANGO_ENV python manage.py migrate
        echo -e "${GREEN}Migrations complete!${NC}"
        echo ""
    else
        echo -e "${YELLOW}Warning: --migrate specified but no manage.py found${NC}"
    fi
fi

# Summary
echo -e "${GREEN}=== Environment Setup Complete ===${NC}"
echo ""
echo "Worktree: $WORKTREE_DIR"

# Show branch info
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Branch: $BRANCH"

# Check if Claude Code is available
if command -v claude &> /dev/null; then
    echo ""
    echo "Ready to start Claude Code:"
    echo -e "  ${YELLOW}claude${NC}"
fi
