from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import config
from forms.cookies import CookiesForm
from forms.form import Form
from forms.pages.results import ResultsPage


class HomePage(Form):
    SEARCH_INPUT_FIELD_LOCATOR = (By.XPATH, "//input[@id='search']")

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.SEARCH_INPUT_FIELD_LOCATOR)

    def is_cookies_form_displayed(self) -> bool:
        return CookiesForm(self.driver).is_displayed()

    def search(self, s) -> ResultsPage:
        search_input_field = self.driver.find_element(*self.SEARCH_INPUT_FIELD_LOCATOR)
        search_input_field.click()
        search_input_field.send_keys(s)
        search_input_field.send_keys(Keys.ENTER)

        return ResultsPage(self.driver)

