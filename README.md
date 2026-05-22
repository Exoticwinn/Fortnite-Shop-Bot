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

Или используйте файл `.env` (если хотите), но в текущей версии проект читает переменную окружения `TELEGRAM_TOKEN`.

## Запуск

```bash
python main.py
```

## Структура проекта

- `main.py` — основная логика Telegram-бота
- `config.py` — получает токен из переменной окружения
- `requirements.txt` — список зависимостей

## Примечание

В `config.py` токен не хранится напрямую, чтобы не попадать в репозиторий. Замените `your_bot_token_here` на свой токен в переменной `TELEGRAM_TOKEN`.
