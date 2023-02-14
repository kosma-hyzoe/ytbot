from helpers import constants
import config
from forms.cookies import CookiesForm
from forms.pages.home import HomePage
from helpers.helpers import get_driver, init_logger


def main():
    init_logger()
    driver = get_driver()
    try:
        driver.get(constants.BASE_URL)
        home_page = HomePage(driver)

        if home_page.is_cookies_form_displayed():
            cookies_form = CookiesForm(driver)
            cookies_form.accept_cookies()
            driver.refresh()

        results_page = home_page.search("10 hours")
        watch_page = results_page.select_first_result()

        if watch_page.is_ads_overlay_displayed():
            watch_page.skip_or_wait_ad()

        watch_page.skip_to_middle()
        watch_page.mute_video()
        watch_page.get_video_details()


    finally:
        driver.quit()


if __name__ == "__main__":
    main()
