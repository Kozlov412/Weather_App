# Погодное приложение

Простое приложение для отображения погоды с использованием Python, requests и plyer.

## Установка

1. Клонируйте репозиторий.
2. Создайте виртуальное окружение.
3. Активируйте виртуальное окружение.
4. Установите зависимости: `pip install -r requirements.txt`

## Запуск

`python WeatherApp.py`

## Упаковка в EXE

`pyinstaller --onefile --noconsole --hidden-import plyer.platforms.win.notification WeatherApp.py`