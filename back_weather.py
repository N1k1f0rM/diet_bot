import requests
from typing import Dict, Tuple, Optional
from config import Secrets, info_logger, error_logger


def get_cords(city: str) -> Optional[Tuple[float, float]]:
  try:

    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={Secrets.WEATHER_TOKEN}")
    response.raise_for_status()
    location = response.json()[0]
    lon, lat = location["lon"], location["lat"]

    info_logger.info(f"Получены данные для {city}: долгота {lon}, широта {lat}")

    return lon, lat

  except requests.RequestException as e:
    error_logger.error(f"Ошибка {e}")


def current_temp(lat: float, lon: float) -> float:
  try:

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=metric&appid={Secrets.WEATHER_TOKEN}")
    temperature = response.json()["main"]["temp"]

    info_logger.info(f"Текущая температура: {temperature}")

    return temperature

  except requests.RequestException as e:
    error_logger.error(f"Ошибка {e} при обращении к {response}")
