import sys

from loguru import logger

from ytbot import config
from ytbot.browser.browser import ChromeBrowser
from ytbot.pages.home import HomePage

BASE_URL = "https://www.youtube.com/"


def run():
    browser = ChromeBrowser()

    try:
        browser.navigate(BASE_URL)
        browser.switch_to_primary_window()

        home_page = HomePage(browser.driver)

        if home_page.is_cookies_form_displayed():
            home_page.accept_cookies()

        results_page = home_page.search(config.SEARCH_STRING)
        watch_page = results_page.select_first_result()

        if watch_page.is_ads_overlay_displayed():
            watch_page.skip_or_wait_ads()

        watch_page.skip_to_middle()
        watch_page.mute_video()

        video_details = watch_page.get_video_details()
        print(f'\n{video_details}\n')

        next_video_watch_page = watch_page.navigate_to_first_suggested_video()

        if next_video_watch_page.is_ads_overlay_displayed():
            next_video_watch_page.skip_or_wait_ads()

        next_video_watch_page.pause_on_duration(config.NEXT_VIDEO_PAUSE_ON_DURATION)
    finally:
        browser.quit()


def init_logger(level: str = config.LOGGER_DEFAULT_LEVEL):
    logger.remove(0)
    logger.add(sys.stderr, level=level, colorize=config.LOGGER_COLORIZE, format=config.LOGGER_FORMAT)


if __name__ == "__main__":
    init_logger()
    run()
