from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from ytbot import config
from loguru import logger
from ytbot.pages.form import Form


class CookiesForm(Form):
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//button[.//span[contains(text(), 'Accept all')]]")

    def __init__(self, driver, timeout=config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.ACCEPT_COOKIES_BUTTON)
        self.driver = driver

    def accept_cookies(self):
        logger.info(f"{self.name}: attempting to accept cookies...")
        accept_cookies_button = self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON)
        accept_cookies_button.click()

    def is_displayed(self) -> bool:
        try:
            return self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).is_displayed()
        except NoSuchElementException:
            return False

