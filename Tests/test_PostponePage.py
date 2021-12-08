import pytest
from Config.config import TestData
from Pages.PostponePage import PostponePage
from Tests.test_base import BaseTest


# to run all tests command: pytest Tests/test_PostponePage.py
# to run all tests and log to html format: pytest Tests/test_PostponePage.py -v --html=./hubSpot.html to
# run all tests and log
# to html format in parallel mode execution: pytest Tests/test_PostponePage.py -v -n 3 --html=./hubSpot.html


class TestPostponeAtHomePage(BaseTest):

    # find first book at home page, click to "heart"="Отложить" button
    def test_first_book_postponed(self):
        self.postponePage = PostponePage(self.driver)
        self.postponePage.accept_cookies_policy()
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        assert first_book.is_enabled()

    # to check that popup window appeared after click to "heart"="Отложить" button
    def test_popup_book_postponed_appeared(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        popup_postponed = self.postponePage.find_one_element(PostponePage.POPUP_BOOK_POSTPONED)
        self.postponePage.scroll_to_element(popup_postponed)
        assert self.postponePage.is_visible(PostponePage.POPUP_BOOK_POSTPONED)

    # to check that popup window show that book postponed disappeared after click to "close" button
    def test_popup_book_postponed_closed(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        popup_postponed = self.postponePage.find_one_element(PostponePage.POPUP_BOOK_POSTPONED)
        self.postponePage.scroll_to_element(popup_postponed)
        assert self.postponePage.is_visible(PostponePage.POPUP_BOOK_POSTPONED)
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        assert self.postponePage.is_not_visible(PostponePage.POPUP_BOOK_POSTPONED)

    # find first book at home page, click to "heart"="Отложить" button and check the quantity of postponed books at
    # the header
    def test_quantity_of_postponed_books_at_the_header(self):
        self.postponePage = PostponePage(self.driver)
        self.postponePage.clear_postpone_reload_page()
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        quantity_text_value_after = self.postponePage.get_element_text(PostponePage.QUANTITY_OF_POSTPONED_BOOKS)
        assert int(quantity_text_value_after) == 1

    # postpone several books and check the quantity is match with quantity at the header
    def test_quantity_of_postponed_books_at_the_header_numerous_selection(self):
        self.postponePage = PostponePage(self.driver)
        self.postponePage.clear_postpone_reload_page()
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        self.selected_books = self.list_of_books[0:3]
        for book in self.selected_books:
            self.postponePage.scroll_to_element(book)
            book.click()
        quantity_text_value = self.postponePage.get_element_text(PostponePage.QUANTITY_OF_POSTPONED_BOOKS)
        assert int(quantity_text_value) == 3

    # test that button "Убрать из отложенных" which appears after click to "heart"="Отложить" button at previously
    # postponed book remove the book from Postponed and quantity of postponed book is one book less
    @pytest.mark.xfail
    def test_for_postponed_book_deletion_by_submenu_of_postpone_book(self):
        self.postponePage = PostponePage(self.driver)
        self.postponePage.clear_postpone_reload_page()
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        quantity_text_value = self.postponePage.get_element_text(PostponePage.QUANTITY_OF_POSTPONED_BOOKS)
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.DELETE_POSTPONED_BOOK)
        new_quantity_text_value = self.postponePage.get_element_text(PostponePage.QUANTITY_OF_POSTPONED_BOOKS)
        assert int(quantity_text_value) - int(new_quantity_text_value) == 1

    # test that name of the book marked as postponed at the home page is equal book name at the postpone page
    def test_that_postponed_book_name_equal_to_book_added(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        self.list_of_book_names = self.postponePage.find_several_element(PostponePage.BOOKS_DESCRIPTION_COVER)
        first_book_cover = self.list_of_book_names[0].get_attribute(TestData.ATTRIBUTE_TITLE)
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        postponed_book_at_postpone_page = self.postponePage.get_element_text(PostponePage.BOOK_IN_POSTPONE_PAGE)
        assert postponed_book_at_postpone_page in first_book_cover

    # test to delete all postponed book at Postpone page by "Очистить" button
    def test_deletion_of_all_books_postponed_at_postpone_page(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        first_book.click()
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.postponePage.do_click(PostponePage.CLEAR_POSTPONE_BUTTON)
        alert = self.driver.switch_to.alert
        alert.accept()
        assert self.postponePage.get_element_text(PostponePage.POSTPONED_BOOKS_DELETED_MESSAGE) == TestData.SUCCESSFUL_DELETION

    # test that "Выделить все" button enable checkboxes of all books at Postpone book page
    def test_that_enable_all_button_work(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        for book in self.list_of_books:
            self.postponePage.scroll_to_element(book)
            book.click()
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.list_of_postponed_books = self.postponePage.find_several_element(PostponePage.CHECKBOX_POSTPONED_BOOKS)
        self.postponePage.do_click(PostponePage.SELECT_ALL_POSTPONED_BOOKS)
        for postponed_book in self.list_of_postponed_books:
            assert postponed_book.is_enabled()

    # test that "Удалить" button appears if any of checkboxes enabled delete selected books from DOM (all books in this test)
    def test_that_delete_button_in_popup_work(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        for book in self.list_of_books:
            self.postponePage.scroll_to_element(book)
            book.click()
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        self.postponePage.do_click(PostponePage.SELECT_ALL_POSTPONED_BOOKS)
        self.all_books_to_be_deleted_list = self.postponePage.find_several_element(PostponePage.ALL_SELECTED_BOOKS)
        self.postponePage.do_click(PostponePage.DELETE_SELECTED_BOOKS)
        alert = self.driver.switch_to.alert
        alert.accept()
        for deleted_book in self.all_books_to_be_deleted_list:
            assert self.postponePage.element_is_not_visible(deleted_book)

    # test that postponed book from Postpone page "Отложено" can be moved into Basket "Корзина" by button "В КОРЗИНУ"
    # which is placed below postponed book at the Postpone page and status of button "В КОРЗИНУ" changed to "ОФОРМИТЬ"
    def test_that_button_move_into_basket_changed_to_checkout(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        # click to move book to Postpone page
        first_book.click()
        # close popup window that book was postponed
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        # switch to Postpone page
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        # find all buttons "В КОРЗИНУ" at the Postpone page
        self.list_of_postponed_books = self.postponePage.find_several_element(PostponePage.MOVE_IN_BASKET_FM_POSTPONE_BUTTON)
        # click to "В КОРЗИНУ" button at first book (which was last added into Postpone page)
        last_postponed_book = self.list_of_postponed_books[0]
        self.postponePage.scroll_to_element(last_postponed_book)
        # read the id of book of book before click
        id_of_book_to_be_postponed = last_postponed_book.get_attribute(TestData.ATTRIBUTE_ID)
        last_postponed_book.click()
        # close popup window that book was moved into Basket
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_POSTPONED_BOOK_MOVED_IN_BASKET)
        self.postponePage.refresh_current_url()
        # find all buttons "ОФОРМИТЬ"
        self.list_of_book_to_be_checked_out = self.postponePage.find_several_element(PostponePage.SWITCH_TO_CHECKOUT_BOOK_IN_BASKET_FM_POSTPONE_PAGE)
        # read the id of book last added to "ОФОРМИТЬ"
        last_book_added_to_checkout = self.list_of_book_to_be_checked_out[0]
        self.postponePage.scroll_to_element(last_book_added_to_checkout)
        id_of_book_to_be_checked_out = last_book_added_to_checkout.get_attribute(TestData.ATTRIBUTE_ID)
        assert id_of_book_to_be_postponed == id_of_book_to_be_checked_out

    # test that after pressing button "В КОРЗИНУ" displayed below book with status "В КОРЗИНУ" at Postpone page,
    # the counter at basket "Корзина" at the header will change quantity of books at basket
    def test_that_button_move_in_below_postponed_book_basket_will_increase_basket_counter(self):
        self.postponePage = PostponePage(self.driver)
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        first_book = self.list_of_books[0]
        self.postponePage.scroll_to_element(first_book)
        # click to move book to Postpone page
        first_book.click()
        # close popup window that book was postponed
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        # switch to Postpone page
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        # get current quantity of books in Basket "Корзина"
        initial_quantity_of_books_in_basket = self.postponePage.get_element_text(TestData.BASKET_COUNTER)
        # find all buttons "В КОРЗИНУ" at the Postpone page
        self.list_of_postponed_books = self.postponePage.find_several_element(PostponePage.MOVE_IN_BASKET_FM_POSTPONE_BUTTON)
        # click to "В КОРЗИНУ" button at first book (which was last added into Postpone page)
        last_postponed_book = self.list_of_postponed_books[0]
        self.postponePage.scroll_to_element(last_postponed_book)
        last_postponed_book.click()
        # close popup window that book was moved into Basket
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_POSTPONED_BOOK_MOVED_IN_BASKET)
        self.postponePage.refresh_current_url()
        new_quantity_of_books_in_basket = self.postponePage.get_element_text(TestData.BASKET_COUNTER)
        assert int(new_quantity_of_books_in_basket) - int(initial_quantity_of_books_in_basket) == 1

    # test that book same name was postponed at the Home page into Postpone page and that added to Basket
    def test_that_same_book_was_postponed_then_moved_to_basket(self):
        self.postponePage = PostponePage(self.driver)
        # find all "Отложить" buttons at home page
        self.list_of_books = self.postponePage.find_several_element(PostponePage.HEART_SYMBOL_AT_HOME_PAGE)
        # selecting first book in the list
        first_book = self.list_of_books[0]
        # find name of all books at Home page
        self.list_of_book_names = self.postponePage.find_several_element(PostponePage.BOOKS_DESCRIPTION_COVER)
        # find name of book at Home page
        first_book_name = self.list_of_book_names[0].get_attribute(TestData.ATTRIBUTE_TITLE)
        self.postponePage.scroll_to_element(first_book)
        # click to move book to Postpone page
        first_book.click()
        # close popup window that book was postponed
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_BOOK_POSTPONED)
        # switch to Postpone page
        self.postponePage.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        # find all buttons "В КОРЗИНУ" at the Postpone page
        self.list_of_postponed_books = self.postponePage.find_several_element(PostponePage.MOVE_IN_BASKET_FM_POSTPONE_BUTTON)
        # find names of all books at Postpone page
        # find "В КОРЗИНУ" button at first book (which was last added into Postpone page)
        last_postponed_book = self.list_of_postponed_books[0]
        # find name of last postponed book at the page
        self.list_of_postponed_book_names = self.postponePage.find_several_element(PostponePage.BOOK_IN_POSTPONE_PAGE)
        name_of_last_postponed_book = self.list_of_postponed_book_names[0].text
        # click to "В КОРЗИНУ" button at first book (which was last added into Postpone page)
        self.postponePage.scroll_to_element(last_postponed_book)
        last_postponed_book.click()
        # close popup window that book was moved into Basket
        self.postponePage.do_click(PostponePage.CLOSE_POPUP_POSTPONED_BOOK_MOVED_IN_BASKET)
        self.postponePage.refresh_current_url()
        # find all books names in basket
        self.list_of_book_names_in_basket = self.postponePage.find_several_element(PostponePage.BOOK_IN_POSTPONE_PAGE)
        # find name of last added into basket book
        last_added_in_basket_name = self.list_of_book_names_in_basket[0].text
        assert name_of_last_postponed_book == last_added_in_basket_name
        assert last_added_in_basket_name in first_book_name
