from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.broko.ai/design-overview")
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("dalepaige@yopmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("P@ss1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Enter Location, MLS or Postal").click()
    page.get_by_placeholder("Enter Location, MLS or Postal").fill("Missi")
    page.get_by_text("Mississauga").nth(2).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
