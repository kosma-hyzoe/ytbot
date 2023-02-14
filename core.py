import config
import constants
from forms.cookies import CookiesForm
from forms.pages.home import HomePage
from helpers import get_driver


def main():
    driver = get_driver()
    try:
        driver.get(constants.BASE_URL)
        home_page = HomePage(driver)

        if home_page.is_cookies_form_displayed():
            cookies_form = CookiesForm(driver)
            cookies_form.accept_cookies()
            driver.refresh()

        results_page = home_page.search(config.SEARCH_STRING)
        results_page.select_first_result()

        print("foobar")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()