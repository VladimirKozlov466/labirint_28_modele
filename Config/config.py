from selenium.webdriver.common.by import By


class TestData:
    CHROME_EXECUTABLE_PATH = "/Users/driverChrome/chromedriver"
    FIREFOX_EXECUTABLE_PATH = "/Users/vladimirkozlov/Downloads/geckodriver 2"

    BASE_URL = "https://www.labirint.ru/"
    USER_NAME = "qazeeman"
    PASSWORD = "4739196A"

    # HOME PAGE data for main menu testing - testing "Книги" button
    BOOKS_BUTTON_DESCRIPTION = "Книги"
    TITLE_OF_BOOK_PAGE = "Книги"
    TITLE_OF_MAIN_YEAR_BOOK_PAGE = "Главные книги 2021"
    ALL_BOOKS_TITLE = "Книги"
    TEENS_BOOKS_TITLE = "Молодежная литература"
    PERIODICALS_TITLE = "Периодические издания"
    BILINGUAL_TITLE = "Билингвы"
    CHILD_BOOK_TITLE = "Детский досуг"
    MANGA_BOOK_TITLE = "Манга для детей"
    RELIGION_BOOK_TITLE = "Религии мира"

    # CURRENT Region setting
    CITY_TO_SET = "Екатеринбург"
    CURRENT_CITY = "Екатеринбург"

    # equal to "москва" in cyrillic
    CITY_TO_SET_IN_CYRILLIC = "Казань"
    FIRST_CITY_IN_AUTO_ADVICE = "Казань"

    CITY_TO_SET_WRONG_LANGUAGE = "vjcrdf"
    FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC = "Москва"

    # Data for PostponePage tests
    NUMBER_OF_BOOKS_TO_POSTPONE = 3

    # Successful deletion of postponed books message
    SUCCESSFUL_DELETION = "Выбранные товары удалены!"

    # Successful deletion of books from Basket
    YOUR_BASKET_IS_EMPTY_TEXT = "Ваша корзина пуста. Почему?"

    # Names of attributes
    ATTRIBUTE_ID = "id"
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_VALUE = "value"

    # Data for Search page
    AUTHOR_SEARCH = "Лев Толстой"
    SEARCHED_BOOK_NAME = "Война и мир"
    SEARCHED_RUSSIAN_BOOK_NAME_BY_LATIN = "jcnhjd cjrhjdbo" # "остров сокровищ"
    EXPECTED_RESULT_BOOK_NAME = "остров сокровищ"


    """CROSS PAGE LOCATORS"""

    # locator for button to close popup which appear after any action ("В Корзину", "ОТЛОЖИТЬ", etc)
    CLOSE_POPUP_ANY_ACTION = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    """for BASKET"""
    # locator for Basket "Корзина" button at header
    BASKET_BUTTON_AT_HEADER = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]')
    # locator for Basket "Корзина" counter
    BASKET_COUNTER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')


    """for Search"""
