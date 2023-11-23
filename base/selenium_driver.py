from selenium.webdriver.common.by import By


class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type: str):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "css_Selector":
            return By.CSS_SELECTOR
        elif locator_type == "xpath":
            return By.XPATH
        else:
            print(f'locator type -->{locator_type} is not correct')
        return False



