import time
import allure

from pages.actions import get_value_h1
from pages.blog_page import BlogPage
from pages.feedback_page import FeedbackPage
from pages.main_page import MainPage
from playwright.sync_api._generated import Page

from pages.webinars_page import WebinarsPage


@allure.suite("Проверка ссылок на главной странице Иннополиса")
class TestGoPagesFromMain:
    @allure.title("Успешный переход в раздел Отзыв из меню главной страницы")
    def test_open_feedback(self, browser_page: Page, main_page: MainPage):
        with allure.step("Открыть главную страницу сайта Иннополис"):
            browser_page.goto(main_page.url)
        with allure.step(f"Перейти в раздел {main_page.feedback}, и проверить что URL раздела корректный"):
            page_feedback = main_page.click_feedback(browser_page=browser_page).value
            time.sleep(10)
            assert page_feedback.url == FeedbackPage.url, f"Некорректный URL в разделе {main_page.feedback}"
        with allure.step(f"Проверить, что на странице есть заголовок {FeedbackPage.heading}"):
            heading_on_page = get_value_h1(page=page_feedback)
            assert heading_on_page == FeedbackPage.heading, f"В разделе отсутствует заголовок {FeedbackPage.heading}"

    @allure.title("Успешный переход в раздел Блог из меню главной страницы")
    def test_open_blog(self, browser_page: Page, main_page: MainPage):
        with allure.step("Открыть главную страницу сайта Иннополис"):
            browser_page.goto(MainPage.url)
        with allure.step(f"Перейти в раздел {main_page.blog}, и проверить что URL раздела корректный"):
            page_blog = main_page.click_blog(browser_page=browser_page).value
            time.sleep(10)
            assert page_blog.url == BlogPage.url, f"Некорректный URL в разделе {main_page.blog}"
        with allure.step(f"Проверить, что на странице есть заголовок {BlogPage.heading}"):
            heading_on_page = get_value_h1(page=page_blog)
            assert heading_on_page == BlogPage.heading, f"В разделе отсутствует заголовок {BlogPage.heading}"

    @allure.title("Успешный переход в раздел Вебинары из меню главной страницы")
    def test_open_webinars(self, browser_page: Page, main_page: MainPage):
        with allure.step("Открыть главную страницу сайта Иннополис"):
            browser_page.goto(MainPage.url)
        with allure.step(f"Перейти в раздел {main_page.webinars}, и проверить что URL раздела корректный"):
            page_webinars = main_page.click_webinars(browser_page=browser_page).value
            time.sleep(10)
            assert page_webinars.url == WebinarsPage.url, f"Некорректный URL в разделе {main_page.webinars}"
        with allure.step(f"Проверить, что на страница есть заголовок {WebinarsPage.heading}"):
            heading_on_page = get_value_h1(page=page_webinars)
            assert heading_on_page == WebinarsPage.heading, f"В разделе отсутствует заголовок {WebinarsPage.heading}"
