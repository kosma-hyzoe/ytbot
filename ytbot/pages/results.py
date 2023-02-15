from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from ytbot import config
from ytbot.pages.form import Form
from ytbot.pages.watch import WatchPage


class ResultsPage(Form):
    SEARCH_INPUT_FIELD_LOCATOR = (By.XPATH, "//input[@id='search']")
    FILTER_MENU_LOCATOR = (By.ID, "filter-menu")
    VIDEO_THUMBNAIL_LOCATOR = (By.ID, "thumbnail")
    VIDEO_TITLE_LOCATOR = (By.ID, "video-title")
    FIRST_RESULT_RELATIVE_LOCATOR = locate_with(*VIDEO_THUMBNAIL_LOCATOR).below(
        {SEARCH_INPUT_FIELD_LOCATOR[0]: SEARCH_INPUT_FIELD_LOCATOR[1]})

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.FILTER_MENU_LOCATOR)

        if "results" not in self.driver.current_url and "YouTube" not in self.driver.title:
            error_message = f"{self.name}: URL doesn't match the pattern, possibly a redirection error"
            logger.error(error_message)
            raise Exception(error_message)

        self.wait_until_is_displayed()

    def select_first_result(self) -> WatchPage:
        first_result = self.driver.find_element(self.FIRST_RESULT_RELATIVE_LOCATOR)

        first_result_title_relative_locator = locate_with(*self.VIDEO_TITLE_LOCATOR).to_right_of(first_result)
        first_result_title = self.driver.find_element(first_result_title_relative_locator)
        logger.info(f"{self.name}: clicking on first result: '{first_result_title.text}'...")
        first_result.click()
        return WatchPage(self.driver)


