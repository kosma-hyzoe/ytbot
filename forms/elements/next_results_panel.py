from selenium.webdriver.common.by import By


class NextResultsPanel:
    VIDEO_TITLE_LOCATOR = (By.ID, "video-title")

    def __init__(self, element):
        self.element = element

    def navigate_to_first_suggested_video(self):
        self.element.find_elements(*self.VIDEO_TITLE_LOCATOR)[0].click()

