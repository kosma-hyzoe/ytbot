from ytbot import config
from ytbot.forms.cookies import CookiesForm
from ytbot.forms.pages.home import HomePage
from ytbot.helpers import get_driver, init_logger, switch_to_primary_window


BASE_URL = "https://www.youtube.com/"


def run():
    init_logger()
    driver = get_driver()

    try:
        driver.get(BASE_URL)
        switch_to_primary_window(driver)

        home_page = HomePage(driver)

        if home_page.is_cookies_form_displayed():
            cookies_form = CookiesForm(driver)
            cookies_form.accept_cookies()
            driver.refresh()

        results_page = home_page.search(config.SEARCH_STRING + "3 hours")
        watch_page = results_page.select_first_result()

        if watch_page.is_ads_overlay_displayed():
            watch_page.skip_or_wait_ad()

        watch_page.skip_to_middle()
        watch_page.mute_video()

        video_details = watch_page.get_video_details()
        print(video_details)

        next_video_watch_page = watch_page.navigate_to_first_suggested_video()

        if next_video_watch_page.is_ads_overlay_displayed():
            next_video_watch_page.skip_or_wait_ad()

        next_video_watch_page.pause_on_duration(config.NEXT_VIDEO_PAUSE_ON_DURATION)
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
