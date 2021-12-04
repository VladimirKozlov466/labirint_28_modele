from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""
"""it contains all the generic methods and utilities for all pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def find_one_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    """to find several elements"""
    def find_several_element(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return elements

    """to display submenu"""
    def move_to_show_submenu(self, by_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()

    """to display submenu and click element at first level"""
    def move_to_submenu_and_click_at_first_level(self, by_locator, submenu_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()
        submenu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(submenu_locator))
        submenu.click()

    """to display submenu and move to element at first level and click element at second level"""
    def move_to_submenu_and_click_at_second_level(self, by_locator, submenu_locator, second_level_locator):
        main_menu = self.find_one_element(by_locator)
        action = ActionChains(self.driver)
        action.move_to_element(main_menu).perform()
        submenu = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(submenu_locator))
        action.move_to_element(submenu).perform()
        second_level_submenu = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(second_level_locator))
        second_level_submenu.click()

