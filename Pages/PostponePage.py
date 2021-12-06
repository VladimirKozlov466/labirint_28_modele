from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class PostponePage(BasePage):
    """By locators - OR"""
    URL = TestData.BASE_URL

    # locator for "Лабиринт" logo by which we can return at home page
    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    # for button "Отложено"
    POSTPONED_BOOKS_BUTTON = (By.XPATH, '//span[@class="b-header-b-personal-e-icon '
                                        'b-header-b-personal-e-icon-m-putorder b-header-e-sprite-background"]')
    # for symbol "heart" - "отложить" for books at Home Page
    HEART_SYMBOL_AT_HOME_PAGE = (By.XPATH, '//a[@data-tooltip_title="Отложить"]')
    # locator for popup window which appears after click to symbol "heart"
    POPUP_BOOK_POSTPONED = (By.XPATH, '//div[contains(text(), "Вы добавили  в отложенные книгу ")]')
    # locator for button which close popup window alerting that book postponed
    CLOSE_POPUP_BOOK_POSTPONED = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """this is used to get the page title"""
    def get_home_page_title(self, title):
        return self.get_title(title)