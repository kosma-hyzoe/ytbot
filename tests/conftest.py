import pytest

from context import ytbot
from ytbot import helpers


@pytest.fixture
def driver():
    driver = helpers.get_driver()
    yield helpers.get_driver()
    driver.quit()


@pytest.fixture()
def logger():
    helpers.init_logger()
