"""
HTML Screenshot Tool

Takes screenshots of HTML files or URLs using Playwright headless browser.
This allows Claude to see what it generated without manual screenshots.

Usage:
    # Screenshot a local HTML file
    poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py <html_file> [output_png]

    # Screenshot an authenticated URL (local dev only - requires DEV_AUTH_ENABLED=True)
    poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py --url <url> --email <user_email> [output_png]

Examples:
    # Screenshot a demo HTML file
    poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py claude/demos/dashboard.html

    # Specify output location
    poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py demo.html /tmp/screenshot.png

    # Full page screenshot (captures entire scrollable content)
    poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py demo.html --full-page

    # Screenshot an authenticated page (local dev only)
    poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py --url http://localhost:8000/candidates/search/ --email cmoore@bayone.com

    # Screenshot authenticated page with custom output
    poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py --url http://localhost:8000/home/ --email user@bayone.com /tmp/home.png
"""

import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

# Default viewport size (desktop)
DEFAULT_WIDTH = 1400
DEFAULT_HEIGHT = 900


async def screenshot_html(
    html_path: str,
    output_path: str = None,
    full_page: bool = False,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    wait_ms: int = 1000
) -> str:
    """
    Take a screenshot of an HTML file.

    Args:
        html_path: Path to the HTML file
        output_path: Where to save the screenshot (default: same dir as HTML, .png extension)
        full_page: If True, capture entire scrollable page
        width: Viewport width
        height: Viewport height
        wait_ms: Milliseconds to wait for page to render (for JS-heavy pages)

    Returns:
        Path to the saved screenshot
    """
    html_path = Path(html_path).resolve()

    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    # Default output path
    if output_path is None:
        output_path = html_path.with_suffix('.png')
    else:
        output_path = Path(output_path).resolve()

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        # Launch headless browser
        browser = await p.chromium.launch(headless=True)

        # Create page with viewport
        page = await browser.new_page(viewport={'width': width, 'height': height})

        # Navigate to the HTML file
        file_url = f"file://{html_path}"
        await page.goto(file_url, wait_until='networkidle')

        # Wait for any JS to render
        if wait_ms > 0:
            await page.wait_for_timeout(wait_ms)

        # Take screenshot
        await page.screenshot(path=str(output_path), full_page=full_page)

        await browser.close()

    return str(output_path)


async def screenshot_url(
    url: str,
    output_path: str,
    full_page: bool = False,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    wait_ms: int = 2000
) -> str:
    """
    Take a screenshot of a URL (unauthenticated).

    Args:
        url: The URL to screenshot
        output_path: Where to save the screenshot
        full_page: If True, capture entire scrollable page
        width: Viewport width
        height: Viewport height
        wait_ms: Milliseconds to wait for page to render

    Returns:
        Path to the saved screenshot
    """
    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': width, 'height': height})

        await page.goto(url, wait_until='networkidle')

        if wait_ms > 0:
            await page.wait_for_timeout(wait_ms)

        await page.screenshot(path=str(output_path), full_page=full_page)

        await browser.close()

    return str(output_path)


async def screenshot_authenticated_url(
    url: str,
    email: str,
    output_path: str,
    base_url: str = "http://localhost:8000",
    full_page: bool = False,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    wait_ms: int = 2000
) -> str:
    """
    Take a screenshot of an authenticated URL using dev auth bypass.

    IMPORTANT: This only works in local development when:
    - DJANGO_ENVIRONMENT=local
    - DEV_AUTH_ENABLED=True in .env.local

    This will NOT work in stage or production environments.

    Args:
        url: The URL to screenshot (must be on the same base_url)
        email: User email to authenticate as
        output_path: Where to save the screenshot
        base_url: Base URL of the Django server (default: http://localhost:8000)
        full_page: If True, capture entire scrollable page
        width: Viewport width
        height: Viewport height
        wait_ms: Milliseconds to wait for page to render

    Returns:
        Path to the saved screenshot

    Example:
        await screenshot_authenticated_url(
            url="http://localhost:8000/candidates/search/",
            email="user@bayone.com",
            output_path="/tmp/screenshot.png"
        )
    """
    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': width, 'height': height})
        page = await context.new_page()

        # Step 1: Authenticate via dev auth bypass
        auth_url = f"{base_url}/accounts/dev/auto-login/?email={email}"
        await page.goto(auth_url, wait_until='networkidle')

        # Verify we got a session (check for sessionid cookie)
        cookies = await context.cookies()
        session_cookie = next((c for c in cookies if c['name'] == 'sessionid'), None)
        if not session_cookie:
            await browser.close()
            raise RuntimeError(
                "Dev auth failed - no session cookie. "
                "Ensure DEV_AUTH_ENABLED=True in .env.local and server is running."
            )

        # Step 2: Navigate to the target URL
        await page.goto(url, wait_until='networkidle')

        # Wait for page to render
        if wait_ms > 0:
            await page.wait_for_timeout(wait_ms)

        # Step 3: Take screenshot
        await page.screenshot(path=str(output_path), full_page=full_page)

        await browser.close()

    return str(output_path)


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    # Check for authenticated URL mode
    if '--url' in sys.argv:
        # Authenticated URL screenshot mode
        try:
            url_idx = sys.argv.index('--url')
            url = sys.argv[url_idx + 1]
        except (IndexError, ValueError):
            print("Error: --url requires a URL argument")
            sys.exit(1)

        try:
            email_idx = sys.argv.index('--email')
            email = sys.argv[email_idx + 1]
        except (IndexError, ValueError):
            print("Error: --email required for authenticated screenshots")
            sys.exit(1)

        # Find output path (first arg that's not a flag or flag value)
        output_path = None
        skip_next = False
        for arg in sys.argv[1:]:
            if skip_next:
                skip_next = False
                continue
            if arg in ('--url', '--email'):
                skip_next = True
                continue
            if arg.startswith('--'):
                continue
            if not arg.startswith('http'):
                output_path = arg
                break

        if output_path is None:
            # Generate default output path
            from urllib.parse import urlparse
            parsed = urlparse(url)
            page_name = parsed.path.strip('/').replace('/', '_') or 'home'
            output_path = f"screenshots/{page_name}.png"

        full_page = '--full-page' in sys.argv

        print(f"Taking authenticated screenshot of: {url}")
        print(f"  Authenticating as: {email}")

        try:
            result = asyncio.run(screenshot_authenticated_url(
                url=url,
                email=email,
                output_path=output_path,
                full_page=full_page
            ))
            print(f"Screenshot saved to: {result}")
            print(f"\nTo view in Claude, use: Read({result})")
        except RuntimeError as e:
            print(f"Authentication error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error taking screenshot: {e}")
            sys.exit(1)

    else:
        # Local HTML file mode (original behavior)
        html_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else None
        full_page = '--full-page' in sys.argv

        print(f"Taking screenshot of: {html_path}")

        try:
            result = asyncio.run(screenshot_html(
                html_path=html_path,
                output_path=output_path,
                full_page=full_page
            ))
            print(f"Screenshot saved to: {result}")
            print(f"\nTo view in Claude, use: Read({result})")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error taking screenshot: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
