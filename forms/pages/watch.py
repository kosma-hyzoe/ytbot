from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from forms.elements.watch_metadata import WatchMetadata
from forms.form import Form
from helpers.models import VideoDetails


class WatchPage(Form):
    VIDEO_LOCATOR = (By.XPATH, "//video")

    ADS_OVERLAY_LOCATOR = (By.XPATH, "//div[contains(@class, 'ytp-ad-player-overlay')]")
    AD_PREVIEW_TEXT_LOCATOR = (By.XPATH, "//div[contains(@class, 'ytp-ad-preview-text')]")
    SKIP_ADS_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'ytp-ad-skip-button')]")

    PROGRESS_BAR_LOCATOR = (By.XPATH, "//div[contains(@class, 'ytp-progress-bar-container')]")
    MUTE_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'ytp-mute-button')]")

    WATCH_METADATA_SECTION_LOCATOR = (By.ID, 'above-the-fold')

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.VIDEO_LOCATOR)

    def skip_to_middle(self):
        progress_bar = self.driver.find_element(*self.PROGRESS_BAR_LOCATOR)
        progress_bar_width = progress_bar.size['width']
        ActionChains(self.driver).click_and_hold(progress_bar).move_by_offset(
            progress_bar_width // 200, 0).release().perform()

    def is_ads_overlay_displayed(self):
        try:
            ads_overlay = self.driver.find_element(*self.ADS_OVERLAY_LOCATOR)
            return ads_overlay.is_displayed()
        except NoSuchElementException:
            return False

    def mute_video(self):
        mute_button = self.driver.find_element(*self.MUTE_BUTTON_LOCATOR)
        mute_button.click()

    def skip_or_wait_ad(self):
        wait = WebDriverWait(self.driver, config.AD_SKIP_TIMEOUT)
        try:
            skip_ads_button = wait.until(EC.visibility_of_element_located(self.SKIP_ADS_BUTTON_LOCATOR))
            skip_ads_button.click()
        except TimeoutException:
            wait.until(EC.invisibility_of_element_located(self.ADS_OVERLAY_LOCATOR))

    def get_video_details(self):
        watch_metadata = self._get_watch_metadata_element()
        print(watch_metadata.get_title())
        print(watch_metadata.get_channel_name())
        print("foobar")

    def _get_watch_metadata_element(self):
        watch_metadata_element = self.driver.find_element(*self.WATCH_METADATA_SECTION_LOCATOR)
        return WatchMetadata(watch_metadata_element)

