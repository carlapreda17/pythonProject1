from playwright.sync_api import Page, sync_playwright

def test_login(page:Page):
    page.goto("https://autoutil.thedemo.is/")
    page.get_by_role("button", name="INTRĂ ÎN CONT").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("carla_preda@yahoo.com")
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").fill("Testare123@")
    page.get_by_role("button", name="INTRĂ ÎN CONT").click()

    page.wait_for_timeout(1000)




