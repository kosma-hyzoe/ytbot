from loguru import logger


def get_video_time_with_js(browser, video_element):
    logger.trace("getting elapsed video time with JavaScript executor...")
    return browser.execute_script("return arguments[0].currentTime;", video_element)
