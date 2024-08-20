from dataclasses import dataclass

from pages.actions import click_link
from playwright.sync_api._generated import Page


@dataclass()
class MainPage:
    url: str = "https://stc.innopolis.university/"
    feedback: str = "Отзывы"
    blog: str = "Блог"
    webinars: str = "Вебинары"

    def click_feedback(self, browser_page: Page):
        return click_link(browser_page=browser_page,
                          name=self.feedback)

    def click_blog(self, browser_page: Page):
        return click_link(browser_page=browser_page,
                          name=self.blog)

    def click_webinars(self, browser_page: Page):
        return click_link(browser_page=browser_page,
                          name=self.webinars)