import pytest
import time
from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


# to run all tests command: pytest Tests/test_HomePage.py
# to run all tests and log to html format: pytest Tests/test_LoginPage.py -v --html=./hubSpot.html
# to run all tests and log to html format in parallel mode execution: pytest Tests/test_LoginPage.py -v -n 3 --html=./hubSpot.html


class TestHomePageMainMenu(BaseTest):

    # test that button "Книги" exits
    def test_books_button_visible(self):
        self.homePage = HomePage(self.driver)
        button = self.homePage.is_visible(HomePage.BOOKS)
        assert button == True

    # test that button "Книги" has proper name
    def test_books_button_has_proper_name(self):
        self.homePage = HomePage(self.driver)
        button_name = self.homePage.get_element_text(HomePage.BOOKS)
        assert button_name == TestData.BOOKS_BUTTON_DESCRIPTION

    # test button "Книги" is clickable and leads to proper page
    def test_books_button_clickable(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_click(HomePage.BOOKS)
        book_page_header = self.homePage.get_element_text(HomePage.BOOKS_PAGE_HEADER)
        assert book_page_header == TestData.TITLE_OF_BOOK_PAGE

    # test submenu "Главное 2021" of button "Книги" is clickable and leads to proper page - submenu "Главное 2021"
    def test_submenu_books_of_year_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.MAIN_OF_THE_YEAR)
        books_main_of_the_year_title = self.homePage.get_element_text(HomePage.MAIN_OF_THE_YEAR_HEADER)
        assert books_main_of_the_year_title == TestData.TITLE_OF_MAIN_YEAR_BOOK_PAGE

    # test submenu "Все книги" of button "Книги" is clickable and leads to proper page - submenu "Книги"
    def test_submenu_all_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.ALL_BOOKS)
        all_books_title = self.homePage.get_element_text(HomePage.ALL_BOOKS_HEADER)
        assert all_books_title == TestData.ALL_BOOKS_TITLE

    # test submenu "Молодежная литература" of button "Книги" is clickable and leads to proper page - submenu "Книги"
    def test_submenu_teens_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.TEENS_BOOKS)
        teens_books_title = self.homePage.get_element_text(HomePage.TEENS_BOOKS_HEADER)
        assert teens_books_title == TestData.TEENS_BOOKS_TITLE

    # test submenu "Периодические издания" of button "Книги" is clickable and leads to proper page - submenu "Книги"
    def test_periodicals_books_in_book_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.move_to_submenu_and_click_at_first_level(HomePage.BOOKS, HomePage.PERIODICAL_BOOKS)
        periodicals_title = self.homePage.get_element_text(HomePage.PERIODICAL_BOOKS_HEADER)
        assert periodicals_title == TestData.PERIODICALS_TITLE
