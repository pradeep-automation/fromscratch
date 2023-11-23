from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    _email_field = "username"
    _pass_field = "password"
    _login_button = "//button[@type='submit']"

    def set_email(self, email):
        self.driver.find_element(self.get_by_type("name"), self._email_field).send_keys(email)

    def set_pass(self, pwd):
        self.driver.find_element(self.get_by_type("name"), self._pass_field).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(self.get_by_type("xpath"), self._login_button).click()
