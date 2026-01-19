import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    expect(page).to_have_title("Great Indian Festival")
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("shoes for ")
    page.get_by_role("button", name="shoes for woman").click()
    with page.expect_popup() as page1_info:
        page.locator(".a-link-normal.s-no-outline").first.click()
    page1 = page1_info.value
    page1.get_by_role("button", name="Add to Cart").click()
    page1.get_by_role("button", name="Add to Cart", exact=True).click()
    page1.locator("#sw-gtc").get_by_role("link", name="Go to Cart").click()
    page1.close()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test1(playwright)
