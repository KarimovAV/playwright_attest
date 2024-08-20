from playwright.sync_api._generated import Page
from playwright._impl._sync_base import T


def click_link(browser_page: Page, name: str):
    with browser_page.expect_popup() as page_click:
        browser_page.get_by_role("link", name=name, exact=True).click()
    return page_click


def get_value_h1(page: T = None, locator: str = "h1"):
    return page.locator(locator).text_content()

