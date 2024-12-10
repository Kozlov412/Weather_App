import requests
from plyer import notification
import os

# Конфигурация
CITY = "Пенза"
API_KEY = "23496c2a58b99648af590ee8a29c5348" #  API ключ от OpenWeatherMap
UNITS = "metric"
LANG = "ru"
APP_NAME = "Weather App"

def get_weather_data(city, api_key, units, lang):
    """Получает данные о погоде от OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={lang}"
    try:
        response = requests.get(url)
        response.raise_for_status() # Проверка на ошибки HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

def parse_weather_data(weather_data):
    """Извлекает нужные данные из JSON ответа."""
    if weather_data:
        try:
            return {
                "temp": weather_data["main"]["temp"],
                "feels_like": weather_data["main"]["feels_like"],
                "description": weather_data["weather"][0]["description"],
            }
        except KeyError as e:
            print(f"Ошибка парсинга данных: {e}")
            return None
    return None

def show_notification(title, message, app_name):
  
    try:
        notification.notify(
            title=title,
            message=message,
            app_name=app_name,
            timeout=10
        )
    except Exception as e:
        print(f"Ошибка отображения уведомления: {e}")    