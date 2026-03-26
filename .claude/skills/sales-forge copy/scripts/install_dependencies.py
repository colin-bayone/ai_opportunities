#!/usr/bin/env python3
"""
Install Playwright and browser dependencies for PDF conversion.
"""

import sys
import subprocess


def install_playwright():
    """Install playwright package."""
    print("Installing playwright...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "playwright"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error installing playwright: {result.stderr}")
        return False
    print("  playwright installed successfully")
    return True


def install_browsers():
    """Install Playwright browsers (Chromium)."""
    print("Installing Chromium browser...")
    print("  (This may take a few minutes on first run)")
    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error installing browsers: {result.stderr}")
        return False
    print("  Chromium installed successfully")
    return True


def install_system_deps():
    """Install system dependencies for Playwright (Linux only)."""
    print("Installing system dependencies...")
    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install-deps", "chromium"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"  Warning: Could not install system deps: {result.stderr}")
        print("  You may need to run with sudo or install manually")
        return False
    print("  System dependencies installed")
    return True


def main():
    print("=" * 50)
    print("Installing sales-forge PDF dependencies")
    print("=" * 50)
    print()

    # Check if playwright is already installed
    try:
        import playwright
        print("[OK] playwright already installed")
        playwright_ok = True
    except ImportError:
        playwright_ok = install_playwright()

    if not playwright_ok:
        print("\nFailed to install playwright. Please install manually:")
        print("  pip install playwright")
        sys.exit(1)

    # Install browsers
    browser_ok = install_browsers()

    if not browser_ok:
        print("\nFailed to install Chromium. Trying system deps first...")
        install_system_deps()
        browser_ok = install_browsers()

    if not browser_ok:
        print("\nFailed to install Chromium browser. Please install manually:")
        print("  python -m playwright install chromium")
        print("  python -m playwright install-deps chromium  # Linux only")
        sys.exit(1)

    print()
    print("=" * 50)
    print("Installation complete!")
    print("=" * 50)
    print()
    print("You can now convert HTML to PDF:")
    print("  python3 html_to_pdf.py input.html output.pdf")


if __name__ == "__main__":
    main()
