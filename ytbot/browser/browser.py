import os

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ytbot import config


class ChromeBrowser:
    EXTENSIONS_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), './extensions'))

    @property
    def driver(self):
        return self._driver

    def __init__(self):
        logger.debug("initiating a chrome browser...")
        options = webdriver.ChromeOptions()

        for option in config.CHROME_OPTIONS:
            logger.debug(f"adding option: {option}")
            options.add_argument(option)

        for extension_filename in os.listdir(self.EXTENSIONS_DIR):
            logger.debug(f"adding extension: {extension_filename}")
            options.add_extension(os.path.join(self.EXTENSIONS_DIR, extension_filename))

        self._driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        logger.info("chrome browser ready")

    def navigate(self, url: str):
        logger.info(f"navigating: {url}")
        self.driver.get(url)

    def switch_to_primary_window(self):
        primary_window = self.driver.window_handles[0]
        logger.debug(f"switching to primary window '{primary_window}'...")
        self.driver.switch_to.window(primary_window)

    def execute_script(self, script, *args):
        logger.debug(f"executing script '{script}' with args '{args}'...")
        self.driver.execute_script(script, *args)

    def refresh(self):
        logger.info("refreshing browser...")
        self.driver.refresh()

    def close(self):
        logger.info("closing browser window...")
        self.driver.close()

    def quit(self):
        logger.info("quitting browser...")
        self.driver.quit()




