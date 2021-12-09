import pytest
from Config.config import TestData
from Pages.BasketPage import BasketPage
from Tests.test_base import BaseTest


# to run all tests command: pytest Tests/test_BasketPage.py
# to run all tests and log to html format: pytest Tests/test_BasketPage.py -v --html=./hubSpot.html to
# run all tests and log
# to html format in parallel mode execution: pytest Tests/test_BasketPage.py -v -n 3 --html=./hubSpot.html


class TestBasketFmHomePage(BaseTest):

    # this test find first book at home page and get price of book than move this book into Basket and check price of
    # this book in the Basket doesn't changing
    def test_first_book_moved_in_basket_and_price_is_same(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.accept_cookies_policy()
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # find all buttons "В КОРЗИНУ" at Home page
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # find add into basket "В КОРЗИНУ" of first book at home page
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # find all prices of all book
        self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # find element which contains price of first book at home page
        first_book_price_element = self.list_of_book_prices[0]
        # get (int) price of first book
        first_book_price = self.basketPage.price_by_int(first_book_price_element)
        # click to button "В КОРЗИНУ" of first book
        fist_book_button_move_into_basket.click()
        # close popup action window
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # click to button "Корзина" at the header
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # find all prices of all book in Basket at Basket page
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # find element which contains price of first book at Basket page
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # get (int) price of first book in Basket
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        assert first_book_price == first_book_price_in_basket

    # this test find first book at home page and get price of book than move this book into Basket and check price of
    # this book in the Basket doesn't changing and equal to final sum of order "Подытог без учета доставки"
    def test_first_book_moved_in_basket_and_price_is_same_and_equal_final_sum(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # find all buttons "В КОРЗИНУ" at Home page
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # find add into basket "В КОРЗИНУ" of first book at home page
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # find all prices of all book
        self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # find element which contains price of first book at home page
        first_book_price_element = self.list_of_book_prices[0]
        # get (int) price of first book
        first_book_price = self.basketPage.price_by_int(first_book_price_element)
        # click to button "В КОРЗИНУ" of first book
        fist_book_button_move_into_basket.click()
        # close popup action window
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # click to button "Корзина" at the header
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # find all prices of all book in Basket at Basket page
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # find element which contains price of first book at Basket page
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # get (int) price of first book in Basket
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # get the final sum of books purchased
        final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
        assert (first_book_price and first_book_price_in_basket) == int(final_sum)

    # this test find first book at home page and get price of book than move this book into Basket and check price of
    # this book in the Basket doesn't changing and equal to final sum of order "Подытог без учета доставки"
    def test_that_button_in_popup_window_leads_to_basket(self):
        self.basketPage = BasketPage(self.driver)
        # find all buttons "В КОРЗИНУ" at Home page
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # find add into basket "В КОРЗИНУ" of first book at home page
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # click to button "В КОРЗИНУ" of first book
        fist_book_button_move_into_basket.click()
        # click to "Оформить" button at popup action window
        self.basketPage.find_several_element(BasketPage.POPUP_CHECKOUT_BOOK_BUTTON)[0].click()
        assert self.basketPage.get_current_url() == BasketPage.BASKET_URL

    # this test check that initial quantity of item (book) added into basket by "В КОРЗИНУ" button is "1" (one piece)
    def test_that_initial_quantity_of_item_added_in_basket_is_one(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # find all buttons "В КОРЗИНУ" at Home page
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # find and add into basket "В КОРЗИНУ" the first book at home page
        self.list_of_buttons_move_into_basket[0].click()
        # close popup action window
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # click to button "Корзина" at the header
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # find all quantity input fields of all items
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # find input field of last added item
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # find quantity of last added item
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) == 1

    # this test check that quantity of item (book) added into basket by "В КОРЗИНУ" button has been increased by
    # pressing button "+"
    def test_that_quantity_of_item_added_in_basket_can_be_increased(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # find all buttons "В КОРЗИНУ" at Home page
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # find and add into basket "В КОРЗИНУ" the first book at home page
        self.list_of_buttons_move_into_basket[0].click()
        # close popup action window
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # click to button "Корзина" at the header
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # find all quantity input fields of all items
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # find input field of last added item
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # find quantity of last added item
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # find all "+" buttons
        self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.INCREASE_QUANTITY_OF_ITEM)
        # increase quantity of last added item for one piece by pressing ones to button "+"
        self.list_of_increase_buttons[0].click()
        # request again quantity of last added item
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(new_quantity_of_first_book) - int(quantity_of_first_book) == 1


