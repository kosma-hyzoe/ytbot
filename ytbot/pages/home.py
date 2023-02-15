from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from loguru import logger
from ytbot import config
from ytbot.pages.form import Form
from ytbot.pages.forms.cookies import CookiesForm
from ytbot.pages.results import ResultsPage


class HomePage(Form):
    SEARCH_INPUT_FIELD_LOCATOR = (By.XPATH, "//input[@id='search']")
    COOKIES_TERMS_AND_CONDITIONS_ELEMENT = (By.ID, "dialog")

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.SEARCH_INPUT_FIELD_LOCATOR)
        self.wait_until_is_displayed()

        if driver.title != "YouTube":
            error_message = f"{self.name}: URL doesn't match the pattern, possibly a redirection error"
            logger.error(error_message)
            raise Exception(error_message)

    def is_cookies_form_displayed(self) -> bool:
        try:
            return self.driver.find_element(*self.COOKIES_TERMS_AND_CONDITIONS_ELEMENT).is_displayed()
        except NoSuchElementException:
            logger.debug(f"{self.name}: NoSuchElementException raised when calling is_cookies_form_displayed()")
            return False

    def accept_cookies(self) -> "HomePage":
        accept_cookies_form = CookiesForm(self.driver)
        accept_cookies_form.accept_cookies()
        accept_cookies_form.wait_until_is_closed()
        return HomePage(self.driver)

    def search(self, s) -> ResultsPage:
        logger.info(f"{self.name}: searching term '{s}'...")
        search_input_field = self.driver.find_element(*self.SEARCH_INPUT_FIELD_LOCATOR)
        search_input_field.click()
        search_input_field.send_keys(s)
        search_input_field.send_keys(Keys.ENTER)

        return ResultsPage(self.driver)

