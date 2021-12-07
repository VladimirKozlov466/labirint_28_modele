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


