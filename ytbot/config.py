# in seconds
DEFAULT_TIMEOUT: float = 5.
LOCATE_AD_OVERLAY_TIMEOUT: float = 1.5
AD_SKIP_TIMEOUT: float = 10.

SEARCH_STRING: str = "python"

# in seconds
NEXT_VIDEO_PAUSE_ON_DURATION: int = 10

# uses 'TRACE', 'DEBUG', 'INFO', 'WARNING' and 'ERROR' loguru levels
LOGGER_DEFAULT_LEVEL: str = "INFO"
LOGGER_DEFAULT_LEVEL_TESTS: str = "DEBUG"
LOGGER_FORMAT: str = "<black><yellow>{level}</yellow> {time:HH:mm:ss.SS} : <green>{message}</green></black>"
LOGGER_COLORIZE: bool = True

CHROME_OPTIONS: list[str] = [
    # '--headless',
]
