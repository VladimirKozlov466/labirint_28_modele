from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class PostponePage(BasePage):
    """By locators - OR"""
    URL = TestData.BASE_URL

    # locator for "Лабиринт" logo by which we can return at home page
    LABIRINT_MAIN_LOGO = (By.XPATH, '//a[@title="Лабиринт - самый большой книжный интернет магазин"]')

    # for button "Отложено"
    # POSTPONED_BOOKS_BUTTON = (By.XPATH, '//span[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-putorder b-header-e-sprite-background"]')
    POSTPONED_BOOKS_BUTTON = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # for symbol "heart" - "отложить" for books at Home Page in chapter "Что почитать: выбор редакции"
    HEART_SYMBOL_AT_HOME_PAGE = (By.XPATH, '//a[@data-tooltip_title="Отложить"]')
    # locator for popup window which appears after click to symbol "heart"
    POPUP_BOOK_POSTPONED = (By.XPATH, '//div[contains(text(), "Вы добавили  в отложенные книгу ")]')
    # locator for button which close popup window alerting that book postponed
    CLOSE_POPUP_BOOK_POSTPONED = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')
    # locator of quantity postponed books at the header of the page
    QUANTITY_OF_POSTPONED_BOOKS = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-putorder basket-in-dreambox-a"]')
    # locator for deletion of book from postponed
    DELETE_POSTPONED_BOOK = (By.XPATH, '//span[@class="b-list-item-hover pointer"]')
    # for description of books in chapter "Что почитать: выбор редакции" displayed at Home page
    BOOKS_DESCRIPTION_COVER = (By.XPATH, '//a[@class="cover"]')
    # locator button "Все отложенные товары" in popup window which appears after moving over "Отложено" icon
    BUTTON_IN_POSTPONE_ICON_POPUP = (By.XPATH, '//a[@class="btn btn-middle btn-clear font_size_s all-putorder-btn-js"]')

    # for book name at "labirint.ru/cabinet/putorder/"=Postponed Book page
    BOOK_IN_POSTPONE_PAGE = (By.XPATH, '//span[@class="product-title"]')

    # locator for button "Очистить" at Postpone page "https://www.labirint.ru/cabinet/putorder/"
    CLEAR_POSTPONE_BUTTON = (By.XPATH, '//a[@title="Удалить все отложенные товары"]')
    # locator for Postpone page message "Сообщение Выбранные товары удалены!"
    POSTPONED_BOOKS_DELETED_MESSAGE = (By.XPATH, '//p[contains(text(),"Выбранные товары удалены!")]')

    # locator for "Выделить все" button  at Postponed page
    SELECT_ALL_POSTPONED_BOOKS = (By.XPATH, '//a[@title="Выделить все отложенные товары"]')
    # locators of checkboxes to mark books at Postponed page
    CHECKBOX_POSTPONED_BOOKS = (By.XPATH, '//label[@class="checkbox-ui checkbox-ui-m-bg checkbox-ui-m-multi checkbox-ui-m-big"]')
    # locator of "Удалить" button in popup menu which appears if any of checkboxes to mark book were enabled
    DELETE_SELECTED_BOOKS = (By.XPATH, '//a[contains(text(),"Удалить")]')
    # locator for brief description of all postponed books at Postponed page
    ALL_SELECTED_BOOKS = (By.XPATH, '//div[@class="product-cover short-title"]')




    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """this is used to get the page title"""
    def get_home_page_title(self, title):
        return self.get_title(title)

    """this method clear postponed books at the Postponed book page and return to Home page. Method was made due to 
    suspection that bag presents in program - cookies not fully removed when page reload after starting new test """
    def clear_postpone_reload_page(self):
        self.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.do_click(PostponePage.CLEAR_POSTPONE_BUTTON)
        alert = self.driver.switch_to.alert
        alert.accept()
        self.do_click(PostponePage.LABIRINT_MAIN_LOGO)

