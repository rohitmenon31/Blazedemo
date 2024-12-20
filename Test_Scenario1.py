import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test() -> None:  # Test function name must start with "test_"
 with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://blazedemo.com/")
    page.locator("select[name=\"fromPort\"]").select_option("San Diego")
    page.locator("select[name=\"toPort\"]").select_option("London")
    page.get_by_role("button", name="Find Flights").click()
    page.get_by_role("row", name="Choose This Flight 234 United").get_by_role("button").click()

    # ---------------------
    context.close()
    browser.close()
