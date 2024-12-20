import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_blazedemo_booking() -> None:  # Test function name must start with "test_"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Test steps
        page.goto("https://blazedemo.com/")
        page.locator("select[name=\"fromPort\"]").select_option("Portland")
        page.locator("select[name=\"toPort\"]").select_option("Berlin")
        page.get_by_role("button", name="Find Flights").click()
        page.get_by_role("row", name="Choose This Flight 9696 Aer").get_by_role("button").click()
        page.get_by_placeholder("First Last").fill("test")
        page.get_by_placeholder("Main St.").fill("test")
        page.get_by_placeholder("Anytown").fill("test")
        page.get_by_placeholder("State").fill("test")
        page.get_by_placeholder("12345").fill("234234")
        page.get_by_role("button", name="Purchase Flight").click()

        # Close browser
        context.close()
        browser.close()
