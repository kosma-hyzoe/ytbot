import sys

from selenium import webdriver
from loguru import logger
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_extension('extensions/return-youtube-dislike.crx')
    return webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


def init_logger():
    logger.remove(0)
    logger.add(sys.stderr, level="INFO", colorize=True,
               format="<black><yellow>[{level}]</yellow>: <green>{message}</green> @ {time:HH:mm:ss.SS}</black>")
