import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test() -> None:
 with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://blazedemo.com/")
    page.locator("select[name=\"fromPort\"]").select_option("Mexico City")
    page.locator("select[name=\"toPort\"]").select_option("Cairo")
    page.get_by_role("button", name="Find Flights").click()
    page.get_by_role("row", name="Choose This Flight 4346").get_by_role("button").click()
    page.get_by_placeholder("First Last").click()
    page.get_by_placeholder("First Last").fill("new123")
    page.get_by_placeholder("Main St.").click()
    page.get_by_placeholder("Main St.").fill("27834")
    page.get_by_placeholder("Anytown").click()
    page.get_by_placeholder("Anytown").fill("nays")
    page.get_by_placeholder("State").click()
    page.get_by_placeholder("State").fill("tate")
    page.get_by_placeholder("12345").click()
    page.get_by_placeholder("12345").fill("2348632874623874623874623")
    page.get_by_label("Remember me").check()
    page.get_by_role("button", name="Purchase Flight").click()
    page.get_by_role("link", name="Travel The World").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
