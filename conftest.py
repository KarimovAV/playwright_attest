import pytest
from playwright.sync_api import Playwright
from playwright.sync_api._generated import Page

from pages.main_page import MainPage


@pytest.fixture(scope="function")
def browser_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    yield context.new_page()
    context.close()
    browser.close()


@pytest.fixture(scope="module")
def main_page() -> MainPage:
    return MainPage()