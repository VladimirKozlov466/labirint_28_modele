from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""This class is the parent of all pages"""
"""it contains all the generic methods and utilities for all pages"""

# locator for button "Принять" accept cookies policy
COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """to find element and click at element"""
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    """to send keys at input field"""
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """to clear search field, send keys at search field"""
    def clear_text_and_send_text(self, by_locator, text):
        input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(input_field).click().pause(2)
        input_field.clear()
        input_field.send_keys(text)

    """to clear search field, send keys at search field and press ENTER key"""
    def clear_text_and_send_text_with_enter(self, by_locator, text):
        input_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(input_field).click().pause(2)
        input_field.clear()
        input_field.send_keys(text)
        input_field.send_keys(u'\ue007')

    """to clear search field, send keys at search field and press ENTER key"""
    def clear_text_in_element_and_send_text_with_enter(self, element, text):
        action = ActionChains(self.driver)
        action.move_to_element(element).click().pause(2)
        element.clear()
        element.send_keys(text)
        element.send_keys(u'\ue007')

    """to get text at the element"""
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """to check that element is visible"""
    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """to check that elements are visible"""
    def are_visible(self, by_locator) -> bool:
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return bool(elements)

    """to check that element is NOT visible"""
    def is_not_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    """to check that element is NOT visible"""

    def element_is_not_visible(self, by_element) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(by_element))
        return bool(element)

    """to check that element is visible"""

    def element_is_visible(self, by_element) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of(by_element))
        return bool(element)

    """ to get title of the loaded page"""
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    """to find one element"""
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

    """to do!"""
    """to get attribute of element"""
    def get_attribute_value(self, by_locator, attr_name):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        value = element.get_attribute(attr_name)
        return value

    """to scroll into view"""
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """this method accept cookies policy and close popup window if displayed"""
    def accept_cookies_policy(self):
        if self.is_visible(COOKIES_POLICY_BUTTON):
            self.do_click(COOKIES_POLICY_BUTTON)
        else:
            pass

    """this used to refresh currently opened page"""
    def refresh_current_url(self):
        self.driver.get(self.driver.current_url)
        self.driver.refresh()

    """ Returns current browser URL. """
    def get_current_url(self):
        return self.driver.current_url
