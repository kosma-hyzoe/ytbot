from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

import config
from forms.form import Form


class ResultsPage(Form):
    SEARCH_INPUT_FIELD_LOCATOR = (By.XPATH, "//input[@id='search']")
    RESULTS_CONTENTS_LOCATOR = (By.ID, "contents")
    VIDEO_THUMBNAIL_LOCATOR = (By.ID, "thumbnail")
    FIRST_RESULT_RELATIVE_LOCATOR = locate_with(*VIDEO_THUMBNAIL_LOCATOR).below({By.XPATH: "//input[@id='search']"})

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.RESULTS_CONTENTS_LOCATOR)

    def select_first_result(self):
        first_result = self.driver.find_element(self.FIRST_RESULT_RELATIVE_LOCATOR)
        first_result.click()


