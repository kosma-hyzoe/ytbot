from selenium.webdriver.common.by import By


class WatchMetadata:
    VIDEO_TITLE_LOCATOR = (By.XPATH, "//h1[contains(@class, 'ytd-watch-metadata')]")
    CHANNEL_LINK_LOCATOR = (By.XPATH, "//div[@id='text-container' and contains(@class, 'ytd-channel-name')]//a")

    def __init__(self, element):
        self.element = element

    def get_title(self) -> str:
        return self.element.find_element(*self.VIDEO_TITLE_LOCATOR).text

    def get_channel_name(self) -> str:
        return self.element.find_element(*self.CHANNEL_LINK_LOCATOR).text
