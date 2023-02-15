from loguru import logger
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ytbot import config
from ytbot.pages.form import Form
from ytbot.pages.elements.video_footer import VideoFooter
from ytbot.parsing import parse_video_duration, parse_view_count, parse_upload_date, parse_like_count
from ytbot.browser.js_utils import get_video_time_with_js
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

        if "watch" not in self.driver.current_url and "YouTube" not in self.driver.title:
            error_message = f"{self.name}: URL doesn't match the pattern, possibly a redirection error"
            logger.error(error_message)
            raise Exception(error_message)

        self.wait_until_is_displayed()

    def skip_to_middle(self):
        slider = self.driver.find_element(*self.PROGRESS_BAR_LOCATOR)
        slider_width = slider.size['width']
        xoffset = slider_width / 200
        logger.info(f"{self.name}: skipping to the middle of video playback with Selenium ActionChains...")
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(xoffset=xoffset, yoffset=0).release().perform()

    def is_ads_overlay_displayed(self, timeout: float = config.LOCATE_AD_OVERLAY_TIMEOUT) -> bool:
        try:
            ads_overlay = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.ADS_OVERLAY_LOCATOR))
            return ads_overlay.is_displayed()
        except TimeoutException:
            logger.debug(f"{self.name}: TimeoutException raised when calling is_ads_overlay_displayed()")
            return False

    def mute_video(self):
        logger.info(f"{self.name}: muting the video...")
        mute_button = self.driver.find_element(*self.MUTE_BUTTON_LOCATOR)
        mute_button.click()

    def skip_or_wait_ads(self):
        wait = WebDriverWait(self.driver, config.AD_SKIP_TIMEOUT)
        logger.info(f"{self.name}: attempting to skip or wait an ad...")

        while self.is_ads_overlay_displayed():
            try:
                skip_ads_button = wait.until(EC.visibility_of_element_located(self.SKIP_ADS_BUTTON_LOCATOR))
                skip_ads_button.click()
            except TimeoutException:
                logger.debug(f"{self.name}: TimeoutException raised when attempting to skip or wait an ad")
                wait.until(EC.invisibility_of_element_located(self.ADS_OVERLAY_LOCATOR))

    def get_video_details(self) -> VideoDetails:
        logger.info(f"{self.name} extracting video details...")
        video_duration = parse_video_duration(self.driver.find_element(*self.VIDEO_DURATION_LOCATOR).text)

        video_footer = VideoFooter(self.driver.find_element(*self.VIDEO_FOOTER_LOCATION))
        video_footer.show_more()

        formatted_view_count = parse_view_count(video_footer.get_view_count())
        formatted_upload_date = parse_upload_date(video_footer.get_upload_date())
        formatted_like_count = parse_like_count(video_footer.get_like_count())
        formatted_dislike_count = parse_like_count(video_footer.get_dislike_count())

        return VideoDetails(
            title=video_footer.get_title(),
            channel_name=video_footer.get_channel_name(),
            upload_date=formatted_upload_date,
            duration=video_duration,
            view_count=formatted_view_count,
            like_count=formatted_like_count,
            dislike_count=formatted_dislike_count
        )

    def navigate_to_first_suggested_video(self) -> "WatchPage":
        next_results_panel = self.driver.find_element(*self.NEXT_RESULTS_PANEL_LOCATOR)
        next_video_title = next_results_panel.find_elements(*self.VIDEO_TITLE_LOCATOR)[0]
        logger.info(f"{self.name}: navigating to first suggested video: '{next_video_title.text}'...")
        next_video_title.click()
        return WatchPage(self.driver)

    def pause_on_duration(self, duration_in_seconds: int):
        video_element = self.driver.find_element(*self.VIDEO_LOCATOR)
        play_pause_button = self.driver.find_element(*self.PLAY_OR_PAUSE_BUTTON_LOCATOR)
        logger.info(f"{self.name}: attempting to pause video when duration reaches {duration_in_seconds} seconds...")
        current_time = get_video_time_with_js(self.driver, video_element)
        while current_time < duration_in_seconds:
            current_time = get_video_time_with_js(self.driver, video_element)
        play_pause_button.click()
        logger.info(f"{self.name}: video paused")