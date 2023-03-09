import re
from playwright.sync_api import Page, sync_playwright


def test_run(page: Page):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://autoutil.thedemo.is/")
    page.get_by_role("button", name="INTRĂ ÎN CONT").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("carla_preda@yahoo.com")
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").press("CapsLock")
    page.locator("input[type=\"password\"]").press("CapsLock")
    page.locator("input[type=\"password\"]").fill("Testare123@")
    page.get_by_role("button", name="INTRĂ ÎN CONT").click()
    page.locator("div:nth-child(2) > div > div > div:nth-child(2) > div").click()
    page.get_by_text("Deconectare").click()
    page.get_by_role("button", name="DA", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
