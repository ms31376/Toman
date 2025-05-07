
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import configs


class LoginPage(BasePage):

    LOGIN_URL = configs.base_url + 'users/login/'
    PROFILE_URL = configs.base_url +'profile/'


    username_selector = (By.NAME, "username")
    otp_code_selector = (By.NAME, "code")
    password_selector = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button[type=submit]")
    toast_locator = (By.ID, "snackbar-container")

    def get_toast_message(self):
        try:
            toast = self.find_element(self.toast_locator)
            return toast.text
        except:
            return None
        
    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def login_with_sms(self, phone_number):
        self.fill_input(self.username_selector,phone_number)
        self.click(self.login_button)
        otp_code_sms = input('enter sms/email code:')
        self.fill_input(self.otp_code_selector,otp_code_sms)

    def login_with_email(self, email,password):
        self.fill_input(self.username_selector,email)
        self.click(self.login_button)
        toast_message = self.get_toast_message()
        print(toast_message)
        if toast_message:
            return toast_message 
        self.fill_input(self.password_selector, password)
        self.click(self.login_button)
        return None  

    def go_to_profile(self):
        self.driver.get(self.PROFILE_URL)


