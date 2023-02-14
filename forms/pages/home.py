from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

import config
from forms.cookies import CookiesForm
from forms.form import Form


class HomePage(Form):
    SEARCH_INPUT_FIELD_LOCATOR = (By.ID, "search-input")

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.SEARCH_INPUT_FIELD_LOCATOR)

    def is_cookies_form_displayed(self) -> bool:
        return CookiesForm(self.driver).is_displayed()