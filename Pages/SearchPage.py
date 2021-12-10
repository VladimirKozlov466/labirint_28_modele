from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage

class SearchPage(BasePage):

    """By locators - OR"""
    URL = TestData.BASE_URL + "search/"

    # locator for "Лабиринт" logo by which we can return at home page
    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    # locator for button "Принять" accept cookies policy
    COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')

    # locator for Search input field at the header "Поиск по Лабиринту"
    SEARCH_FIELD = (By.ID, "search-field")
    # locator for Search submit button
    SEARCH_SUBMIT = (By.XPATH, '//button[@class="b-header-b-search-e-btn"]')

    # locator for Author name
    AUTHOR_NAME = (By.XPATH, '//div[@class="product-author"]/a')
    





    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SearchPage.URL)

    """Page Actions"""

    """to check if all "search words" are in text result if result was searched in attribute value"""
    def search_match_fully(self, element, search_name):
        element_text = element.get_attribute(TestData.ATTRIBUTE_TITLE)
        element_in_list = element_text.lower().split()
        name_list = search_name.lower().split()
        result = list(set(element_in_list) & set(name_list))
        return len(name_list) == len(result)

