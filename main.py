import telebot
import random
import requests
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
API_URL = "https://fortnite-api.com/v2/shop?language=ru"

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=["start", "help"])
def send_help(message):
    bot.send_message(message.chat.id, "Привет! /shop — магазин, /random — случайный предмет")

def fetch_shop():
    resp = requests.get(API_URL, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    entries = data.get("data", {}).get("entries", [])
    items = []
    for entry in entries:
        name = (
            entry.get("devName")
            or entry.get("legoKits", [{}])[0].get("name")
            or entry.get("items", [{}])[0].get("name")
            or "Unknown"
        )
        image = (
            entry.get("newDisplayAsset", {}).get("renderImages", [{}])[0].get("image")
            or entry.get("items", [{}])[0].get("images", {}).get("icon")
            or entry.get("items", [{}])[0].get("images", {}).get("background")
        )
        price = entry.get("finalPrice", "Unknown")
        items.append({"name": name, "price": price, "image": image})
    return items

@bot.message_handler(commands=["shop"])
def send_shop(message):
    try:
        items = fetch_shop()
    except Exception:
        bot.send_message(message.chat.id, "Ошибка получения магазина.")
        return
    if not items:
        bot.send_message(message.chat.id, "Магазин сейчас пуст.")
        return
    text = "\n".join(
        f"{i+1}. {item['name']} — {item['price']} V-Bucks"
        for i, item in enumerate(items[:20])
    )
    bot.send_message(message.chat.id, text)
    first_image = items[0].get("image")
    if first_image:
        bot.send_photo(
            message.chat.id,
            first_image,
            caption=f"{items[0]['name']} — {items[0]['price']} V-Bucks"
        )

@bot.message_handler(commands=["random"])
def send_random(message):
    try:
        items = fetch_shop()
    except Exception:
        bot.send_message(message.chat.id, "Ошибка получения магазина.")
        return
    if not items:
        bot.send_message(message.chat.id, "Магазин сейчас пуст.")
        return
    item = random.choice(items)
    caption = f"{item['name']} — {item['price']} V-Bucks"
    if item.get("image"):
        bot.send_photo(message.chat.id, item["image"], caption=caption)
    else:
        bot.send_message(message.chat.id, caption)

bot.polling(none_stop=True)