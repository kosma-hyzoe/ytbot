import pytest

import helpers


@pytest.fixture
def driver():
    driver = helpers.get_driver()
    yield helpers.get_driver()
    driver.quit()
