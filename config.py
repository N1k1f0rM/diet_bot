from dotenv import load_dotenv
from dataclasses import dataclass
import logging
import shutil
import os


load_dotenv()


@dataclass
class Secrets:
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
    WEATHER_TOKEN: str = os.environ.get("API_WEATHER_TOKEN")
    FOOD_TOKEN: str = os.environ.get("API_FOOD_TOKEN")


def setup_loggers(logger_path):

    if not os.path.exists(logger_path):
        os.mkdir(logger_path)


    info_logger = logging.getLogger()
    info_logger.setLevel(logging.INFO)
    info_handler = logging.FileHandler(os.path.join(logger_path, "info.log"))
    info_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    info_handler.setFormatter(formatter)
    info_logger.addHandler(info_handler)

    error_logger = logging.getLogger("error_logger")
    error_logger.setLevel(logging.ERROR)
    error_handler = logging.FileHandler(os.path.join(logger_path, "error.log"))
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    error_logger.addHandler(error_handler)

    return info_logger, error_logger


info_logger, error_logger = setup_loggers("logs")