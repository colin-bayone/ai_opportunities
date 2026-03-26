#!/usr/bin/env python3
"""
Check if Playwright dependencies are installed for PDF conversion.
Exit codes:
  0 - All dependencies installed
  1 - Dependencies missing (run install_dependencies.py)
"""

import sys
import subprocess


def check_playwright():
    """Check if playwright is installed."""
    try:
        import playwright
        return True
    except ImportError:
        return False


def check_playwright_browsers():
    """Check if Playwright browsers are installed."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "playwright", "install", "--dry-run", "chromium"],
            capture_output=True,
            text=True
        )
        # If dry-run succeeds without needing to download, browsers are installed
        return "chromium" not in result.stdout.lower() or result.returncode == 0
    except Exception:
        return False


def main():
    print("Checking sales-forge dependencies...")
    print()

    issues = []

    # Check Playwright
    if check_playwright():
        print("[OK] playwright package installed")
    else:
        print("[MISSING] playwright package not installed")
        issues.append("playwright")

    # Check browsers (only if playwright is installed)
    if check_playwright():
        # Try to import and check
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                try:
                    browser = p.chromium.launch(headless=True)
                    browser.close()
                    print("[OK] Chromium browser available")
                except Exception as e:
                    print(f"[MISSING] Chromium browser not installed")
                    issues.append("chromium")
        except Exception as e:
            print(f"[MISSING] Playwright browsers not configured: {e}")
            issues.append("browsers")

    print()

    if issues:
        print("Some dependencies are missing.")
        print("Run: python3 {baseDir}/scripts/install_dependencies.py")
        print()
        print("Or manually:")
        if "playwright" in issues:
            print("  pip install playwright")
        if "chromium" in issues or "browsers" in issues:
            print("  python -m playwright install chromium")
        sys.exit(1)
    else:
        print("All dependencies installed. Ready for PDF conversion.")
        sys.exit(0)


if __name__ == "__main__":
    main()
