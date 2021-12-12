import time

import pytest
from Config.config import TestData
from Pages.SearchPage import SearchPage
from Tests.test_base import BaseTest


# to run all tests command: pytest Tests/test_SearchPage.py
# to run all tests and log to html format: pytest Tests/test_SearchPage.py -v --html=./hubSpot.html to
# run all tests and log
# to html format in parallel mode execution: pytest Tests/test_SearchPage.py -v -n 3 --html=./hubSpot.html


class TestSearchPage(BaseTest):

    # this test check if Author searched presents in displayed book's author names
    def test_search_by_author(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.accept_cookies_policy()
        # find search string and enter Author name
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.AUTHOR_SEARCH)
        # find author names after search done
        self.search_result_list = self.searchPage.find_several_element(SearchPage.AUTHOR_NAME)
        # check if author searched is in author names of books displayed in result
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.AUTHOR_SEARCH):
                counter += 1
            else:
                counter = counter
        assert counter > 0

    # this test check if Author searched presents in displayed book's description
    def test_that_search_by_author_made_in_book_description(self):
        self.searchPage = SearchPage(self.driver)
        # find search string and enter Author name
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.AUTHOR_SEARCH)
        # find book's description after search done
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        # check if author searched is in description of books displayed in result
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.AUTHOR_SEARCH):
                counter += 1
            else:
                counter = counter
        assert counter > 0

    # this test check that search by book name works in Cyrillic
    def test_that_search_by_book_name_works(self):
        self.searchPage = SearchPage(self.driver)
        # find search string and enter book name
        self.searchPage.clear_text_and_send_text_with_enter(SearchPage.SEARCH_FIELD, TestData.SEARCHED_BOOK_NAME)
        # find book's description after search done
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        # check if author searched is in description of books displayed in result
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.SEARCHED_BOOK_NAME):
                counter += 1
            else:
                pass
        assert counter > 0

    # this test check that search by book name works if words in Cyrillic typed in Latin
    def test_that_search_by_book_name_works_if_russian_word_typed_by_latin(self):
        self.searchPage = SearchPage(self.driver)
        # find search string and send book name (russian word in latin)
        self.searchPage.clear_text_and_send_text(SearchPage.SEARCH_FIELD, TestData.SEARCHED_RUSSIAN_BOOK_NAME_BY_LATIN)
        # find Submit Search button and click to start search and check that button works
        self.searchPage.do_click(SearchPage.SEARCH_SUBMIT)
        # find book's description after search done
        self.search_result_list = self.searchPage.find_several_element(SearchPage.BOOK_DESCRIPTION)
        # check if author searched is in description of books displayed in result
        counter = 0
        for search_result in self.search_result_list:
            if self.searchPage.search_match_fully(search_result, TestData.EXPECTED_RESULT_BOOK_NAME):
                counter += 1
            else:
                pass
        assert counter > 0

    # this test check that Button "ВСЕ ФИЛЬТЫ" displayed at the page body open hiding Submenu "ВСЕ ФИЛЬТЫ"
    # and digital books will be removed from search page after clicking button "Электронные книги"
    def test_that_submenu_search_opens_and_disabling_digital_books_works(self):
        self.searchPage = SearchPage(self.driver)
        # find all books which contains label "Электронные книги" below book cover image
        self.list_of_digital_books = self.searchPage.find_several_element(SearchPage.DIGITAL_BOOKS_LABEL)
        # find elements of "ВСЕ ФИЛЬТРЫ" button and click to button
        button_to_open_all_filters = self.searchPage.find_several_element(SearchPage.ALL_FILTERS)
        # click to button to show hidden submenu "ВСЕ ФИЛЬТРЫ"
        button_to_open_all_filters[0].click()
        # disable goods with label "Электронные книги" by pressing on button "Электронные книги" at submenu which
        # appears at the left side
        self.searchPage.do_click(SearchPage.DIGITAL_BOOKS_IN_ALL_FILTERS)
        # click to "Показать" button in submenu to perform search
        self.searchPage.do_click(SearchPage.SHOW_RESULTS)
        # check that there are no any books with label "Электронные книги" at the page
        for book in self.list_of_digital_books:
            assert self.searchPage.element_is_not_visible(book)

    # this test check that Button "Бумажные книги" displayed at the page body hiding Submenu "ВСЕ ФИЛЬТЫ" clickable
    # and after click remove from search settings and quick button "Бумажные книги" will disappear from page body
    def test_that_paper_book_button_in_hidden_submenu_remove_quick_button_from_page(self):
        self.searchPage = SearchPage(self.driver)
        # find elements of "ВСЕ ФИЛЬТРЫ" button and click to button
        button_to_open_all_filters = self.searchPage.find_several_element(SearchPage.ALL_FILTERS)
        # click to button to show hidden submenu "ВСЕ ФИЛЬТРЫ"
        button_to_open_all_filters[0].click()
        # disable goods with label "Бумажные книги" by pressing on button "Бумажные книги" at submenu which appears
        # at the left side
        self.searchPage.do_click(SearchPage.PAPER_BOOKS_IN_ALL_FILTERS)
        # click to "Показать" button in submenu to perform search
        self.searchPage.do_click(SearchPage.SHOW_RESULTS)
        # check that quick button "Бумажные книги" disappeared from page body
        assert self.searchPage.is_not_visible(SearchPage.ENABLED_PAPER_BOOKS)

    # this test check that quick button "В наличии" which displayed in string below "ВСЕ ФИЛЬТРЫ" button clickable
    # and after click remove from search page all books with status "В наличии" (means all books with button "В КОРЗИНУ"
    # will disappear from search page)
    def test_that_quick_button_books_available_works(self):
        self.searchPage = SearchPage(self.driver)
        # find all books with button "В КОРЗИНУ" (books available currently)
        self.list_of_currently_available = self.searchPage.find_several_element(SearchPage.BUY_NOW_BUTTON)
        # find quick button "В наличии" which displayed in string below "ВСЕ ФИЛЬТРЫ" button
        self.searchPage.do_click(SearchPage.BOOKS_AVAILABLE_CURRENTLY)
        # check that all books with button "В КОРЗИНУ" has been disappeared
        for book in self.list_of_currently_available:
            assert self.searchPage.element_is_not_visible(book)

