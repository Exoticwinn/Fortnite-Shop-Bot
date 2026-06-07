import telebot
import random
import requests
import time
from config import TOKEN
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Увеличиваем timeout для всех запросов
requests.adapters.DEFAULT_TIMEOUT = 30

bot = telebot.TeleBot(TOKEN)
API_URL = "https://fortnite-api.com/v2/shop?language=ru"

shop_cache = {"items": [], "timestamp": 0}

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, f'👋 Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=["start", "help"])
def send_help(message):
    help_text = """
🎮 <b>Добро пожаловать в Fortnite Shop Bot!</b>

📋 <b>Доступные команды:</b>
/shop — 🛍️ Показать магазин (с навигацией)
/random — 🎲 Случайный предмет
/help — 📖 Помощь

✨ <b>Новое:</b> Используйте кнопки для навигации по магазину!

💡 Просто напишите команду и получите результат!
    """
    bot.send_message(message.chat.id, help_text, parse_mode="HTML")

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

def format_shop_item(item, index=None):
    name = item.get('name', 'Unknown')[:30]
    price = item.get('price', 'Unknown')
    prefix = f"#{index} " if index is not None else ""
    return f"{prefix}💰 <b>{name}</b>\n   💵 {price} V-Bucks\n\n"

@bot.message_handler(commands=["shop"])
def send_shop(message):
    try:
        bot.send_message(message.chat.id, "⏳ Загружаю магазин...")
        items = fetch_shop()
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка получения магазина.\n<code>{str(e)}</code>", parse_mode="HTML")
        return
    if not items:
        bot.send_message(message.chat.id, "🏚️ Магазин сейчас пуст.")
        return
    
    show_shop_page(message.chat.id, items, 0)

def show_shop_page(chat_id, items, page):
    items_per_page = 5
    total_pages = (len(items) + items_per_page - 1) // items_per_page
    
    if page < 0:
        page = 0
    if page >= total_pages:
        page = total_pages - 1
    
    start = page * items_per_page
    end = start + items_per_page
    page_items = items[start:end]
    
    text = f"🛍️ <b>FORTNITE SHOP</b>\n"
    text += f"📄 Страница {page + 1}/{total_pages}\n"
    text += "=" * 30 + "\n\n"
    
    for i, item in enumerate(page_items, start + 1):
        text += format_shop_item(item, i)
    
    keyboard = InlineKeyboardMarkup()
    buttons = []
    
    if page > 0:
        buttons.append(InlineKeyboardButton("⬅️ Назад", callback_data=f"shop_page_{page - 1}"))
    
    buttons.append(InlineKeyboardButton(f"📄 {page + 1}/{total_pages}", callback_data="shop_info"))
    
    if page < total_pages - 1:
        buttons.append(InlineKeyboardButton("Далее ➡️", callback_data=f"shop_page_{page + 1}"))
    
    keyboard.add(*buttons)
    
    try:
        bot.send_message(chat_id, text, parse_mode="HTML", reply_markup=keyboard)
    except:
        bot.send_message(chat_id, text, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("shop_page_"))
def handle_shop_navigation(call):
    try:
        page = int(call.data.split("_")[-1])
        items = fetch_shop()
        
        bot.delete_message(call.message.chat.id, call.message.message_id)
        
        show_shop_page(call.message.chat.id, items, page)
        
        bot.answer_callback_query(call.id, f"📄 Страница {page + 1}")
    except Exception as e:
        bot.answer_callback_query(call.id, f"❌ Ошибка: {str(e)}", show_alert=True)

@bot.message_handler(commands=["random"])
def send_random(message):
    try:
        items = fetch_shop()
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка получения магазина.\n<code>{str(e)}</code>", parse_mode="HTML")
        return
    if not items:
        bot.send_message(message.chat.id, "🏚️ Магазин сейчас пуст.")
        return
    item = random.choice(items)
    item_text = format_shop_item(item)
    caption = f"🎲 <b>СЛУЧАЙНЫЙ ПРЕДМЕТ</b>\n\n{item_text}"
    if item.get("image"): 
        try:
            bot.send_photo(message.chat.id, item["image"], caption=caption, parse_mode="HTML")
        except:
            bot.send_message(message.chat.id, caption, parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, caption, parse_mode="HTML")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.reply_to(message, "❓ Команда не распознана.\n📖 Используйте /help для списка команд", parse_mode="HTML")

print("🚀 Бот запущен и ожидает сообщений...")
print("=" * 40)

import time

retry_count = 0
max_retries = 5

try:
    while retry_count < max_retries:
        try:
            bot.polling(none_stop=True, timeout=60)
        except requests.exceptions.ReadTimeout as e:
            retry_count += 1
            print(f"⏱️  Timeout при подключении к API ({retry_count}/{max_retries})")
            if retry_count < max_retries:
                wait_time = 5 * retry_count
                print(f"⏳ Повтор через {wait_time} сек...")
                time.sleep(wait_time)
            else:
                print("❌ Не удалось подключиться после нескольких попыток")
                break
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            time.sleep(5)
except KeyboardInterrupt:
    print("\n⛔ Бот остановлен")