import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test() -> None:
 with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://blazedemo.com/")
    page.locator("select[name=\"fromPort\"]").select_option("Boston")
    page.get_by_role("button", name="Find Flights").click()
    page.get_by_role("row", name="Choose This Flight 12 Virgin").get_by_role("button").click()
    page.get_by_placeholder("First Last").click()
    page.get_by_placeholder("First Last").fill("sdf")
    page.get_by_role("button", name="Purchase Flight").click()
    page.get_by_role("link", name="home").click()
    page.get_by_role("link", name="Forgot Your Password?").click()

    # ---------------------
    context.close()
    browser.close()
