import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError(
        "Telegram bot token is missing. Set TELEGRAM_TOKEN environment variable."
    )