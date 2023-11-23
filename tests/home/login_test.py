import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage


class LoginTest(unittest.TestCase):

    def test_login(self):
        base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(base_url)
        lp = LoginPage(driver)
        lp.set_email("Admin")
        lp.set_pass("admin123")
        lp.click_login()
        time.sleep(3)
        home_page_text = driver.find_element(By.CSS_SELECTOR, "span[class*='topbar-header']")
        if home_page_text.text == "Dashboard":
            print("Test login successful")
        else:
            print("Test Login failed")

        driver.execute_script("window.scroll(")




