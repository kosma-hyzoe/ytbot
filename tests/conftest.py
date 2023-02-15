import pytest
import loguru

from context import ytbot
from ytbot import config
from ytbot.core import init_logger
from ytbot.browser.browser import ChromeBrowser


@pytest.fixture
def browser():
    browser = ChromeBrowser()
    yield browser
    browser.quit()


@pytest.fixture()
def logger():
    init_logger(level=config.LOGGER_DEFAULT_LEVEL_TESTS)
    yield loguru.logger
