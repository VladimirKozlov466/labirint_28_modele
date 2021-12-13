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
    # locator for book's description which is under book cover
    BOOK_DESCRIPTION = (By.XPATH, '//a[@class="product-title-link"]')

    # locators for Submenu of "ВСЕ ФИЛЬТРЫ"
    # button "ВСЕ ФИЛЬТРЫ" which is in page body and opens hidden submenu at left side
    ALL_FILTERS = (By.XPATH, '//span[@class="navisort-item__content" and contains(text(), "ВСЕ ФИЛЬТРЫ")]')
    # button "Бумажные книги" in submenu "ВСЕ ФИЛЬТРЫ" to enable/disable books from search
    PAPER_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Бумажные книги")]')
    # button "Электронные книги" in submenu "ВСЕ ФИЛЬТРЫ" to enable/disable books from search
    DIGITAL_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Электронные книги")]')
    # button "Показать" down at the end of submenu "ВСЕ ФИЛЬТРЫ" to confirm filter settings
    SHOW_RESULTS = (By.XPATH, '//input[@class="show-goods__button" and @value="Показать"]')
    # button "ЦЕНА" clicking which hidden submenu for price setting appears
    PRICE_MENU_BUTTON = (By.XPATH, '//div[@class="bl-name" and contains(text(), "ЦЕНА")]')
    # input field to set minimum price of items to be searched
    SET_MIN_PRICE = (By.ID, "section-search-form-price_min")
    # input field to set maximum price of items to be searched
    SET_MAX_PRICE = (By.ID, "section-search-form-price_max")

    # locator for quick button which show present search setting displayed at the page body below button "ВСЕ ФИЛЬТРЫ"
    # locator showing that "Бумажные книги" are enabled (this button remove this setting from search when clicked)
    ENABLED_PAPER_BOOKS = (By.XPATH, '//div[contains(text(), "Бумажные книги")]')
    # locator showing that "В наличии" are enabled (this button remove this setting from search when clicked)
    BOOKS_AVAILABLE_CURRENTLY = (By.XPATH, '//div[@class="filter-reset__content" and contains(text(), "В наличии")]')
    ALL_CURRENT_SETTINGS = (By.XPATH, '//div[@class="filter-reset__content"]')

    # locators for elements displayed below book cover
    # locator for label "ЭЛЕКТРОННАЯ КНИГА" which is placed below book cover
    DIGITAL_BOOKS_LABEL = (By.XPATH, '//span[@class="card-label__text card-label__text_inversed" and contains(text(), '
                                     '"Электронная книга")]')
    # locator for button "КУПИТЬ" displayed only if book currently available at store
    BUY_NOW_BUTTON = (By.XPATH, '//a[@class="btn buy-link js-ebooks-buy-btn btn-primary" and contains(text(), '
                                '"КУПИТЬ")]')

    # locator for book price
    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]/span')
    # locator for pagination page button (for test use page 2)
    PAGINATION_PAGE_BUTTON = (By.XPATH, '//a[@class="pagination-next__text" and contains(text(), "Следующая")]')

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

    """to get price of the book"""

    def price_by_int(self, element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)
