from dotenv import load_dotenv
from dataclasses import dataclass
import os


load_dotenv()


@dataclass
class Secrets:
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
    WEATHER_TOKEN: str = os.environ.get("API_WEATHER_TOKEN")
    FOOD_TOKEN: str = os.environ.get("API_FOOD_TOKEN")


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("No token in env")