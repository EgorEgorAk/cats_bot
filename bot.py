import requests
import json
import telebot
from telebot import types
from config import TOKEN
from config import X_api_key

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    # Создаем Inline-клавиатуру
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_button = types.InlineKeyboardButton(text="Send the cat", callback_data="call_main_message")
    inline_keyboard.add(inline_button)
    
    # Создаем Reply-клавиатуру
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    reply_button = types.KeyboardButton("Send the cat 🐈")
    reply_keyboard.add(reply_button)
    
    # Отправляем сообщение с Reply-клавиатурой
    bot.send_message(
        message.chat.id,
        "Привет, я бот, который отправляет котиков.\nНажми кнопку внизу или напиши 'cats', и я отправлю тебе милого котика.",
        reply_markup=reply_keyboard  # Показываем Reply-клавиатуру
    )
    
    # Отправляем Inline-клавиатуру отдельно
    bot.send_message(
        message.chat.id,
        "Нажми кнопку ниже, чтобы получить котика:",
        reply_markup=inline_keyboard
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
        'x-api-key': X_api_key
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    for i in data:
        bot.send_photo(message.chat.id, i["url"])

@bot.message_handler(func=lambda message: message.text == "Send the cat 🐈")
def handle_reply_button(message):
    main_message(message)


 
@bot.message_handler(func=lambda message: True)  # Срабатывает для всех сообщений
def handle_unknown_message(message):
    bot.send_message(message.chat.id, "ОШИБКА: неизвестная команда или сообщение.")

bot.infinity_polling()