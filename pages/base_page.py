import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configs


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = configs.base_url
        self.wait = WebDriverWait(self.driver, configs.default_wait_time)

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def fill_input(self, locator, text):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.clear()
        el.send_keys(text)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_title(self):
        return self.driver.title
    def check_text_in_page():
        return True
