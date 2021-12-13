This repository is my final project of study for QA Python at Skillfactory platform.
Repository has been created by using PageObject pattern with Selenium and PyTest (Python).
Project contains 52 Selenium UI test of online store "Labirint" "https://www.labirint.ru/".

Preparations to start:

copy repository to your machine,
if you are using PyCharm, it automatically "request" to install libraries required,
if not - install libraries required in requirements.txt.

Change following data:
in Config/config.py change path to (actual for your OS and your Browser version) chromedriver and or geckodriver:

for macOS:
    CHROME_EXECUTABLE_PATH = "/path...to/chromedriver"
    FIREFOX_EXECUTABLE_PATH = "/path...to/geckodriver"

for Windows:
    CHROME_EXECUTABLE_PATH = "C:\\path...to\\chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "C:\\path...to\\geckodriver.exe"

in Tests/conftest.py:
if your want to start testing both Firefox and Chrome browsers leave it like (params=["chrome", "firefox"])
if your want to start one by one change for (params=["chrome"]) or (params=["firefox"])

To START test:

to run all tests command:
    for macOS: pytest Tests/* or pytest Tests
    for Windows: pytest Tests

to run all tests and log results to html format:
    for macOS: pytest Tests/* -v --html=./hubSpot.html
    for Windows: pytest Tests -v --html=./hubSpot.html

run all tests and log to html format in parallel mode execution:
    for macOS: pytest Tests/* -v -n 3 --html=./hubSpot.html
    (digit "3" could be changed - set number of simultaneously opened browser)
    for Windows: pytest Tests -v -n 3 --html=./hubSpot.html
    (digit "3" could be changed - set number of simultaneously opened browser)

to run one set of tests: pytest Tests/test_File_Name.py
to run one test: pytest Tests/test_File_Name.py::TestClassName::test_name
