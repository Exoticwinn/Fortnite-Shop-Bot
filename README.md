# Telegram Fortnite Shop Bot

Telegram-бот для просмотра актуального магазина Fortnite с интеграцией REST API.

**Автор:** [Хуаде Руслан]

## Описание

Простой и удобный бот, который позволяет быстро узнать, какие предметы доступны в магазине Fortnite прямо из Telegram. Получайте актуальную информацию о скинах и предметах, не запуская игру.

## Функции

- Просмотр полного магазина Fortnite (/shop)
- Случайный предмет из магазина (/random)
- Интерактивные кнопки навигации
- Поддержка русского языка
- Кеширование данных для быстрого доступа
- Изображения для каждого предмета

## Быстрый старт

### Установка

```bash
# 1. Создайте виртуальное окружение
python -m venv venv

# 2. Активируйте его
venv\Scripts\activate

# 3. Установите зависимости
pip install -r requirements.txt
```

### Настройка токена

1. Найдите [@BotFather](https://t.me/botfather) в Telegram
2. Создайте бота командой `/newbot`
3. Скопируйте токен и установите переменную окружения:

```bash
# Windows
set TELEGRAM_TOKEN=ваш_токен_бота

# macOS/Linux
export TELEGRAM_TOKEN=ваш_токен_бота
```

### Запуск

```bash
python main.py
```

## Структура проекта

```
├── main.py           - Основная логика бота
├── config.py         - Конфигурация и токен
├── requirements.txt  - Зависимости
├── test_bot.py       - Тесты
├── CHECKLIST.md      - Чек-лист проверки
└── HOW_TO_TEST.md    - Руководство по тестированию
```

## Команды

- `/start` — Начало работы и справка
- `/help` — Справка и доступные команды
- `/shop` — Показать текущий магазин
- `/random` — Случайный предмет
- `/hello` — Приветствие

## Технологии

- **pyTelegramBotAPI** (4.12.0) — Работа с Telegram Bot API
- **requests** (2.32.0) — HTTP-запросы к API
- **Fortnite API** — Данные магазина

## Тестирование

```bash
python test_bot.py
```

Смотрите [CHECKLIST.md](CHECKLIST.md) и [HOW_TO_TEST.md](HOW_TO_TEST.md) для подробного тестирования.

## Обратная связь

Нашли баг или есть идея?

- Email: [rus.khuade@inbox.ru]

## Полезные ссылки

- [pyTelegramBotAPI Documentation](https://pytba.readthedocs.io/ru/latest/)
- [Fortnite API](https://fortnite-api.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## Заключение

Этот проект демонстрирует, как создать полезное приложение с интеграцией внешних API и удобным интерфейсом в Telegram. Может быть полезен игрокам, разработчикам и студентам, изучающим работу с API.

---

**Лицензия:** MIT
