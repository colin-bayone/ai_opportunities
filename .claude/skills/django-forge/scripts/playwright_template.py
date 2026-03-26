#!/usr/bin/env python3
"""
Playwright Template Script - Reference Implementation

This script demonstrates the CORRECT patterns for Playwright testing in this project.
Copy and modify this template for new tests.

CRITICAL PATTERNS:
1. Direct URL auth (NOT clicking login buttons)
2. Cookie verification after auth
3. JavaScript click for hidden elements
4. State-based waits (NOT arbitrary timeouts)

Run with: poetry run python .claude/skills/django-forge/scripts/playwright_template.py
"""
import asyncio
import re
from pathlib import Path
from playwright.async_api import async_playwright

# =============================================================================
# CONFIGURATION
# =============================================================================
BASE_URL = "http://localhost:8000"
PROJECT_ROOT = Path("/home/cmoore/programming/talent_ai")
SCREENSHOT_DIR = Path("./playwright_screenshots")


# =============================================================================
# AUTHENTICATION - CORRECT PATTERN
# =============================================================================
def get_dev_auth_email():
    """
    Read DEV_AUTH_USER_EMAIL from .env.local.

    NEVER hardcode email addresses. Always read from .env.local.
    """
    env_local = PROJECT_ROOT / ".env.local"
    if not env_local.exists():
        raise FileNotFoundError(f".env.local not found at {env_local}")

    content = env_local.read_text()
    match = re.search(r'DEV_AUTH_USER_EMAIL=([^\s#]+)', content)
    if not match:
        raise EnvironmentError("DEV_AUTH_USER_EMAIL not found in .env.local")

    return match.group(1).strip()


async def authenticate(page, context):
    """
    Authenticate via dev auth bypass.

    CORRECT: Direct URL to auth endpoint
    WRONG: Clicking login buttons and hoping auth completes

    Returns the authenticated email address.
    """
    email = get_dev_auth_email()

    # CORRECT: Navigate directly to auth endpoint
    await page.goto(f"{BASE_URL}/accounts/dev/auto-login/?email={email}")
    await page.wait_for_load_state('networkidle')

    # CORRECT: Verify auth succeeded by checking session cookie
    cookies = await context.cookies()
    session_cookie = next((c for c in cookies if c['name'] == 'sessionid'), None)

    if not session_cookie:
        raise Exception(f"Authentication failed for {email} - no session cookie")

    return email


# =============================================================================
# CLICKING ELEMENTS - CORRECT PATTERNS
# =============================================================================
async def click_element_js(page, selector):
    """
    Click element via JavaScript, bypassing visibility checks.

    Use this for:
    - Buttons inside scrollable containers
    - Accordion content that may be collapsed
    - Modal triggers in sidebars
    - Any element that exists in DOM but may not be in viewport

    CORRECT: JavaScript direct click
    WRONG: await page.locator(selector).click() for hidden elements
    """
    await page.evaluate(f"""
        const el = document.querySelector('{selector}');
        if (el) {{
            el.click();
        }} else {{
            throw new Error('Element not found: {selector}');
        }}
    """)


async def wait_for_element(page, selector, timeout=5000):
    """
    Wait for element to appear in DOM.

    CORRECT: State-based wait
    WRONG: await page.wait_for_timeout(3000)
    """
    await page.wait_for_selector(selector, timeout=timeout)


# =============================================================================
# SCREENSHOT UTILITIES
# =============================================================================
async def take_screenshot(page, name, full_page=False):
    """Take a screenshot with consistent naming."""
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    path = SCREENSHOT_DIR / f"{name}.png"
    await page.screenshot(path=str(path), full_page=full_page)
    print(f"  ✓ {name}.png saved")
    return path


async def screenshot_element(page, selector, name):
    """Take a screenshot of a specific element."""
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    element = page.locator(selector)
    if await element.count() > 0:
        path = SCREENSHOT_DIR / f"{name}.png"
        await element.screenshot(path=str(path))
        print(f"  ✓ {name}.png saved")
        return path
    else:
        print(f"  ✗ Element not found: {selector}")
        return None


# =============================================================================
# MAIN TEST TEMPLATE
# =============================================================================
async def run_test():
    """
    Main test function - modify this for your specific test.
    """
    print("Starting Playwright Test...")

    # Get email from .env.local (NEVER hardcode)
    dev_email = get_dev_auth_email()
    print(f"Will authenticate as: {dev_email}")

    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()

        try:
            # =================================================================
            # STEP 1: Authenticate
            # =================================================================
            print("Step 1: Authenticating...")
            email = await authenticate(page, context)
            print(f"  ✓ Authenticated as {email}")

            # =================================================================
            # STEP 2: Navigate to test page
            # =================================================================
            print("Step 2: Navigating to test page...")
            test_url = f"{BASE_URL}/candidates/search/?job_role_id=1"
            await page.goto(test_url, wait_until="networkidle")

            # CORRECT: State-based wait for page to settle
            await page.wait_for_load_state('networkidle')
            await asyncio.sleep(1)  # Brief pause for any JS initialization

            await take_screenshot(page, "01_initial_page")

            # =================================================================
            # STEP 3: Interact with elements
            # =================================================================
            print("Step 3: Interacting with elements...")

            # Example: Click a potentially hidden button using JS
            # await click_element_js(page, '[data-bs-target="#myModal"]')

            # Example: Wait for modal to appear
            # await wait_for_element(page, '#myModal.show')

            # Example: Fill a form field
            # await page.fill('#search-input', 'test query')

            # Example: Click a visible button
            # await page.click('#submit-btn')

            # =================================================================
            # STEP 4: Verify results
            # =================================================================
            print("Step 4: Verifying results...")

            # Example: Check element exists
            # assert await page.locator('#success-message').count() > 0

            # Example: Check element text
            # text = await page.locator('#result').inner_text()
            # assert 'expected' in text

            await take_screenshot(page, "02_final_state")

            print("\n✓ Test completed successfully!")

        except Exception as e:
            # Always capture error screenshot
            await take_screenshot(page, "error", full_page=True)
            print(f"\n✗ ERROR: {e}")
            raise

        finally:
            await browser.close()

    print(f"\nScreenshots saved to: {SCREENSHOT_DIR.absolute()}")


# =============================================================================
# ANTI-PATTERNS - DO NOT USE THESE
# =============================================================================
"""
# ❌ WRONG: Clicking login buttons
page.goto("/protected-page/")
page.locator('text=Sign In').click()
page.wait_for_timeout(3000)  # Just hoping auth works

# ❌ WRONG: Arbitrary timeouts
await page.click('#submit')
await page.wait_for_timeout(5000)

# ❌ WRONG: Standard click on hidden elements
await page.locator('button.hidden-in-sidebar').click()  # Will timeout

# ❌ WRONG: Hardcoded email
email = "someuser@example.com"  # NEVER do this
"""


if __name__ == "__main__":
    asyncio.run(run_test())
