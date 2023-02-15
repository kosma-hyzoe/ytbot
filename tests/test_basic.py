from ytbot.core import BASE_URL
from ytbot.pages.home import HomePage


def test_cookies_form_closes_properly(logger, browser):
    browser.navigate(BASE_URL)
    browser.switch_to_primary_window()

    home_page = HomePage(browser.driver)
    assert home_page.is_displayed(), "Failed to display the home page"
    assert home_page.is_cookies_form_displayed(), "Failed to display the cookies form"

    home_page = home_page.accept_cookies()

    assert not home_page.is_cookies_form_displayed(), "Failed to close cookies form"



