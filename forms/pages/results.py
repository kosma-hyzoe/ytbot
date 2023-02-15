from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

import config
from forms.form import Form
from forms.pages.watch import WatchPage


class ResultsPage(Form):
    SEARCH_INPUT_FIELD_LOCATOR = (By.XPATH, "//input[@id='search']")
    FILTER_MENU_LOCATOR = (By.ID, "filter-menu")
    VIDEO_THUMBNAIL_LOCATOR = (By.ID, "thumbnail")
    FIRST_RESULT_RELATIVE_LOCATOR = locate_with(*VIDEO_THUMBNAIL_LOCATOR).below(
        {SEARCH_INPUT_FIELD_LOCATOR[0]: SEARCH_INPUT_FIELD_LOCATOR[1]})

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.FILTER_MENU_LOCATOR)

    def select_first_result(self) -> WatchPage:
        first_result = self.driver.find_element(self.FIRST_RESULT_RELATIVE_LOCATOR)
        first_result.click()
        return WatchPage(self.driver)


