from selenium.webdriver.common.by import By


class VideoFooter:
    VIDEO_TITLE_LOCATOR = (By.XPATH, "//h1[contains(@class, 'ytd-watch-metadata')]")
    CHANNEL_LINK_LOCATOR = (By.XPATH, "//div[@id='text-container' and contains(@class, 'ytd-channel-name')]//a")
    SHOW_MORE_BUTTON_LOCATOR = (By.ID, "expand")
    UPLOAD_DATE_LOCATOR = (By.XPATH, "//*[@id='info']/span[3]")
    VIEWS_COUNT_LOCATOR = (By.XPATH, "//*[@id='info']/span[1]")
    LIKE_BUTTON_LOCATOR = (By.ID, "segmented-like-button")
    DISLIKE_BUTTON_LOCATOR = (By.ID, "segmented-dislike-button")

    def __init__(self, element):
        self.element = element

    def show_more(self):
        show_more_button = self.element.find_element(*self.SHOW_MORE_BUTTON_LOCATOR)
        show_more_button.click()

    def get_title(self) -> str:
        return self.element.find_element(*self.VIDEO_TITLE_LOCATOR).text

    def get_channel_name(self) -> str:
        return self.element.find_element(*self.CHANNEL_LINK_LOCATOR).text

    def get_upload_date(self) -> str:
        return self.element.find_element(*self.UPLOAD_DATE_LOCATOR).text

    def get_view_count(self) -> str:
        return self.element.find_element(*self.VIEWS_COUNT_LOCATOR).text

    def get_like_count(self) -> str:
        return self.element.find_element(*self.LIKE_BUTTON_LOCATOR).text

    def get_dislike_count(self) -> str:
        return self.element.find_element(*self.DISLIKE_BUTTON_LOCATOR).text


