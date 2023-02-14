import sys
import os

from selenium import webdriver
from loguru import logger
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()

    print(os.getcwd())
    options.add_extension('return-youtube-dislike.crx')
    options.add_argument('--disable-extension-welcome-page')

    prefs = {"profile.managed_default_content_settings.images": 2, "profile.default_content_settings.popups": 0,
             "protocol_handler.excluded_schemes": {"chrome-extension": True}}
    options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


def init_logger():
    logger.remove(0)
    logger.add(sys.stderr, level="INFO", colorize=True,
               format="<black><yellow>[{level}]</yellow>: <green>{message}</green> @ {time:HH:mm:ss.SS}</black>")
