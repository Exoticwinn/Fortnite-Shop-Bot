# Telegram Fortnite Shop Bot

Простой Telegram-бот, который показывает магазин Fortnite и случайный предмет.

## Подготовка окружения

1. Создайте виртуальное окружение:

```bash
python -m venv venv
```

2. Активируйте окружение:

```bash
venv\Scripts\activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Задайте токен бота:

```bash
set TELEGRAM_TOKEN=ваш_токен_бота
```

## Запуск

```bash
python main.py
```

## Структура проекта

- `main.py` — основная логика Telegram-бота
- `config.py` — получает токен из переменной окружения
- `requirements.txt` — список зависимостей

## Тип моего проекта
> Telegram-бот, интегрированный с REST API третьей стороны для получения данных магазина

## Библиотеки, которые я буду использовать
- pyTelegramBotAPI — библиотека для работы с Telegram Bot API
- requests — HTTP-клиент для запросов к API Fortnite
- os — работа с переменными окружения для безопасного хранения токенов

## Референсы, которые мне пригодятся
- [pyTelegramBotAPI Documentation] — полная документация по методам и обработчикам сообщений
- [Fortnite API](https://fortnite-api.com/) — документация API для получения данных магазина и предметов
- [Telegram Bot Best Practices]

## Тестирование

```bash
# Запусти простые тесты
python test_bot.py
```

Файлы для тестирования:
- `test_bot.py` — простые тесты
- `CHECKLIST.md` — чек-лист что проверить
- `HOW_TO_TEST.md` — как тестировать

## Гайды-статьи, где есть полезная для меня информация
- Обработка сообщений и команд в боте... [Message Handlers]
- Асинхронные запросы к внешним API... [Requests Documentation](https://docs.python-requests.org/en/latest/)
- Управление токенами и конфиденциальными данными... [Environment Variables Best Practices]
