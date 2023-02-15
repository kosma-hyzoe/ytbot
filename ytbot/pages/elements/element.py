from loguru import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ytbot import config


class Element:

    def __init__(self, element):
        self.name = self.__class__.__name__
        logger.debug(f"{self.name}: initiating...")
        self.element = element
        WebDriverWait(self.element, config.DEFAULT_TIMEOUT).until(EC.visibility_of(element))
