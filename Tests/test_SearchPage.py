import pytest
from Config.config import TestData
from Pages.SearchPage import SearchPage
from Tests.test_base import BaseTest


# to run all tests comman
# to run all tests and log to html format: pytest Tests/test_SearchPage.py -v --html=./hubSpot.html to
# run all tests and log
# to html format in parallel mode execution: pytest Tests/test_PSearchPage.py -v -n 3 --html=./hubSpot.html



class TestPostponeAtHomePage(BaseTest):

    # find first book at home page, click to "heart"="Отложить" button
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