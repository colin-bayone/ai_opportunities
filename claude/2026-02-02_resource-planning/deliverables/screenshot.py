from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath("resource_plan_for_cisco.html")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 900})
    page.goto(f"file://{html_path}")
    page.screenshot(path="mockup_screenshot.png", full_page=True)
    browser.close()
    print("Screenshot saved to mockup_screenshot.png")
