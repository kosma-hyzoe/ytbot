from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class Form(object):
    def __init__(self, driver, timeout: int, unique_element_locator: (By, str)):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.unique_element_locator = unique_element_locator

        self.wait.until(EC.visibility_of_element_located(self.unique_element_locator))

    def is_displayed(self) -> bool:
        try:
            return self.driver.find_element(*self.unique_element_locator).is_displayed()
        except NoSuchElementException:
            return False

    def wait_until_is_closed(self):
        self.wait.until(EC.invisibility_of_element_located(self.unique_element_locator))
