from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage

class HomePage(BasePage):

    """By locators - OR"""
    URL = TestData.BASE_URL
    # locators of main menu bar for button "Книги" and submenu buttons
    BOOKS = (By.XPATH, '//a[@class="b-header-b-menu-e-text" and contains(text(), "Книги")]')
    BOOKS_PAGE_HEADER = (By.XPATH, '//h1[contains(text(), "Книги")]')
    MAIN_OF_THE_YEAR = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Главное 2021")]')
    MAIN_OF_THE_YEAR_HEADER = (By.XPATH, '//h1[contains(text(), "Главные книги 2021")]')


    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """this is used to get the page title"""
    def get_home_page_title(self, title):
        return self.get_title(title)

    """this is used to check sign up link"""

