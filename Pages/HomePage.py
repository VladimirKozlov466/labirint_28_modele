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
    ALL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Все книги")]')
    ALL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Книги")]')
    TEENS_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Молодежная литература")]')
    TEENS_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Молодежная литература")]')
    PERIODICAL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Периодические издания")]')
    PERIODICAL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Периодические издания")]')

    # locators of main menu bar for button "Книги" for books type at second hidden submenu
    BILINGUAL_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Билингвы и книги на иностранных языках")]')
    BILINGUAL_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Билингвы")]')
    BILINGUAL_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Билингвы")]')

    CHILD_BOOKS_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Книги для детей")]')
    CHILD_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Детский досуг")]')
    CHILD_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Детский досуг")]')

    MANGA_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Комиксы, Манга, Артбуки")]')
    MANGA_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Манга для детей")]')
    MANGA_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Манга для детей")]')

    RELIGION_FIRST_SUBMENU = (By.XPATH, '//span[@class="b-menu-list-title b-menu-list-title-first" and contains(text(), "Религия")]')
    RELIGION_BOOKS = (By.XPATH, '//a[@class="b-menu-list-title " and contains(text(), "Религии мира")]')
    RELIGION_BOOKS_HEADER = (By.XPATH, '//h1[contains(text(), "Религии мира")]')

    # locators for setting of user region location
    REGION_ICON_BUTTON = (By.XPATH, '//span[@class="js-header-menu-region-name"]')
    REGION_CURRENT_SETTING = (By.XPATH, '//span[@class="region-location-icon-txt "]')
    REGION_SEARCH_FIELD = (By.ID, "region-post")
    # locator for auto-advice in search region field
    REGION_GUESS_LUST = (By.XPATH, '//a[@class="a-item"]')





    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """this is used to get the page title"""
    def get_home_page_title(self, title):
        return self.get_title(title)

    """this is used to check sign up link"""

