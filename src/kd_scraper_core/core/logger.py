import logging

LOGGER_NAME = "kd_scraper_core"


def get_logger() -> logging.Logger:
    logger = logging.getLogger(LOGGER_NAME)

    if not logger.handlers:
        logging.basicConfig(
            level=logging.INFO,
            format=("%(asctime)s | %(leveltime)s | %(name)s | %(message)s"),
        )

    return logger
