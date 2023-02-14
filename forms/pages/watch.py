from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from forms.form import Form


class WatchPage(Form):
    AD_PREVIEW_TEXT_LOCATOR = (By.XPATH, "//div[contains(@class, 'ytp-ad-preview-text')]")
    SKIP_ADS_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'ytp-ad-skip-button')]")
    VIDEO_LOCATOR = (By.XPATH, "//video")
    ADS_OVERLAY_LOCATOR = (By.XPATH, "//div[contains(@class, 'ytp-ad-player-overlay')]")

    def __init__(self, driver, timeout: int = config.DEFAULT_TIMEOUT):
        super().__init__(driver, timeout, self.VIDEO_LOCATOR)

    def is_ads_overlay_displayed(self):
        try:
            ads_overlay = self.driver.find_element(*self.ADS_OVERLAY_LOCATOR)
            return ads_overlay.is_displayed()
        except NoSuchElementException:
            return False

    def skip_or_wait_ad(self):
        wait = WebDriverWait(self.driver, config.AD_SKIP_TIMEOUT)
        try:
            skip_ads_button = wait.until(EC.visibility_of_element_located(self.SKIP_ADS_BUTTON_LOCATOR))
            skip_ads_button.click()
        except TimeoutException:
            wait.until(EC.invisibility_of_element_located(self.ADS_OVERLAY_LOCATOR))


