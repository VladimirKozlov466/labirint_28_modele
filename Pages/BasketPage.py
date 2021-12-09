from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class BasketPage(BasePage):

    """By locators - OR"""

    BASKET_URL = "https://www.labirint.ru/cart/"

    # locator for "Лабиринт" logo by which we can return at home page
    LABIRINT_MAIN_LOGO = (By.XPATH, '//a[@title="Лабиринт - самый большой книжный интернет магазин"]')

    # locator for button  "В КОРЗИНУ" placed under each book
    MOVE_BOOK_TO_BASKET = (By.XPATH, '//a[@class="btn buy-link btn-primary" and contains(text(), "В КОРЗИНУ")]')
    # locator for book price
    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]')
    # locator for final sum of books purchased at the Basket page
    PURCHASE_FINAL_SUM = (By.ID, "basket-default-sumprice-discount")
    # locator for button "Очистить корзину" at Basket page
    REMOVE_ALL_GOODS_IN_BASKET = (By.XPATH, '//a[@class="b-link-popup" and contains(text(), "Очистить корзину")]')
    # locator for popup window with button "Оформить"
    POPUP_CHECKOUT_BOOK_BUTTON = (By.XPATH, '//a[@class="color_white btn btn-small btn-primary basket-go analytics-click-js"]')
    # locator of input field for quantity of each item (book) in user order at Basket page which is displayed below
    # of each item in Basket
    QUANTITY_OF_EACH_ITEM_IN_BASKET = (By.XPATH, '//input[@class="quantity"]')
    # locator of button "+" increase quantity of item (book) in purchase at Basket page
    INCREASE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-increase btn-increase-cart"]')



    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """to get price of the book"""
    def price_by_int(self, element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)

    """this method delete all books if any in Basket and return to Home page. Method was made due to suspection that 
    bag presents in program - cookies not fully removed when page reload after starting new test """

    def remove_all_good_in_basket_and_reload_page(self):
        quantity = self.get_element_text(TestData.BASKET_COUNTER)
        if int(quantity) != 0:
            self.do_click(TestData.BASKET_BUTTON_AT_HEADER)
            self.do_click(BasketPage.REMOVE_ALL_GOODS_IN_BASKET)
            self.do_click(BasketPage.LABIRINT_MAIN_LOGO)