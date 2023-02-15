from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class Form(object):
    def __init__(self,  driver, timeout: int, unique_element_locator: (By, str)):
        self.name = self.__class__.__name__
        logger.info(f"{self.name}: initiating...")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.unique_element_locator = unique_element_locator

    def is_displayed(self) -> bool:
        try:
            return self.driver.find_element(*self.unique_element_locator).is_displayed()
        except NoSuchElementException:
            logger.debug(f"{self.name}: NoSuchElementException raised when calling is_displayed()")
            return False

    def wait_until_is_displayed(self):
        logger.debug(f"{self.name}: waiting for to be displayed...")
        self.wait.until(EC.visibility_of_element_located(self.unique_element_locator))

    def wait_until_is_closed(self):
        logger.debug(f"{self.name}: waiting for to be closed...")
        self.wait.until(EC.invisibility_of_element_located(self.unique_element_locator))
