
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ytbot import config
from ytbot.forms.elements.video_footer import VideoFooter
from ytbot.forms.form import Form
from ytbot.helpers import get_video_time_with_js
from ytbot.models.video_detals import VideoDetails


class WatchPage(Form):
    VIDEO_LOCATOR = (By.XPATH, "//video")

    ADS_OVERLAY_LOCATOR = (By.XPATH, "//div[contains(@class, 'ytp-ad-player-overlay')]")
    AD_PREVIEW_TEXT_LOCATOR = (By.XPATH, "//div[contains(@class, 'ytp-ad-preview-text')]")
    SKIP_ADS_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'ytp-ad-skip-button')]")

    PROGRESS_BAR_LOCATOR = (By.XPATH, "//div[contains(@class, 'ytp-progress-bar-container')]")
    MUTE_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'ytp-mute-button')]")
    VIDEO_DURATION_LOCATOR = (By.CLASS_NAME, "ytp-time-duration")
    PLAY_OR_PAUSE_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'ytp-play-button')]")

    VIDEO_FOOTER_LOCATION = (By.ID, "above-the-fold")

    NEXT_RESULTS_PANEL_LOCATOR = (By.XPATH, "//div[@id='items' and contains(@class, 'results-renderer')]")
    VIDEO_TITLE_LOCATOR = (By.ID, "video-title")

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.VIDEO_LOCATOR)

    def skip_to_middle(self):
        slider = self.driver.find_element(*self.PROGRESS_BAR_LOCATOR)
        slider_width = slider.size['width']
        xoffset = slider_width / 200
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(xoffset=xoffset, yoffset=0).release().perform()

    def is_ads_overlay_displayed(self) -> bool:
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

    def get_video_details(self) -> VideoDetails:
        video_duration = self.driver.find_element(*self.VIDEO_DURATION_LOCATOR).text

        video_footer = VideoFooter(self.driver.find_element(*self.VIDEO_FOOTER_LOCATION))
        video_footer.show_more()

        return VideoDetails(
            duration=video_duration,
            title=video_footer.get_title(),
            channel_name=video_footer.get_channel_name(),
            upload_date=video_footer.get_upload_date(),
            view_count=video_footer.get_view_count(),
            like_count=video_footer.get_like_count(),
            dislike_count=video_footer.get_dislike_count()
        )

    def navigate_to_first_suggested_video(self) -> "WatchPage":
        next_results_panel = self.driver.find_element(*self.NEXT_RESULTS_PANEL_LOCATOR)
        next_results_panel.find_elements(*self.VIDEO_TITLE_LOCATOR)[0].click()
        return WatchPage(self.driver)

    def pause_on_duration(self, duration_in_seconds: int):
        video_element = self.driver.find_element(*self.VIDEO_LOCATOR)
        play_pause_button = self.driver.find_element(*self.PLAY_OR_PAUSE_BUTTON_LOCATOR)

        current_time = get_video_time_with_js(self.driver, video_element)
        while current_time < duration_in_seconds:
            current_time = get_video_time_with_js(self.driver, video_element)
        play_pause_button.click()