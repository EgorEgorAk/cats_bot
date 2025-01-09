import requests
import json
import telebot
from telebot import types

TOKEN = 'Token'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Send the cat", callback_data="call_main_message")
    keyboard.add(button)
    bot.send_message(
        message.chat.id,
        "Привет, я бот, который отправляет котиков.\nНапиши мне 'cats' или нажми кнопку, и я отправлю тебе милого котика",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data == "call_main_message")
def handle_callback_main_message(call):
    """Обрабатывает callback-запрос для кнопки, вызывающей отправку котика."""
    main_message(call.message)
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda message: message.text.lower() == "cats")
def main_message(message):
    url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'live_eiQcee8Hl47evF38WEsHIzX7M8nJ1HZRxpflNiMbqKMo6rNmxJF89rb0n4I8brRN'
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    for i in data:
        bot.send_photo(message.chat.id, i["url"])

    

bot.infinity_polling()
