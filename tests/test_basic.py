from context import ytbot

from ytbot.main import BASE_URL
from ytbot.helpers import switch_to_primary_window
from ytbot.forms.pages.home import HomePage
from ytbot.forms.cookies import CookiesForm


def test_cookies_form_closes_properly(driver):
    driver.get(BASE_URL)
    switch_to_primary_window(driver)

    home_page = HomePage(driver)
    assert home_page.is_displayed(), "Failed to display the home page"
    assert home_page.is_cookies_form_displayed(), "Failed to display the cookies form"

    cookies_form = CookiesForm(driver)

    cookies_form.accept_cookies()
    cookies_form.wait_until_is_closed()
    assert not cookies_form.is_displayed(), "Failed to close cookies form"



