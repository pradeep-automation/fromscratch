
from selenium import webdriver

base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(base_url)
