import telebot
from telebot import types
from decouple import config

from database import JSONDatabase, Database
from helpers import gen_languages_markup
from geopy.geocoders import Nominatim

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


geolocator = Nominatim(user_agent="telegram_bot")

@bot.message_handler(commands=["start"])
def start(message):
    username = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Hello {username}!",
    )

@bot.message_handler(commands=["geophone"])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Send phone number", request_contact=True)
    button_geo = types.KeyboardButton(text="Send location", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "Please send phone number or location", reply_markup=keyboard)


@bot.message_handler(content_types=["location"])
def handle_location(message):
    location = geolocator.reverse((message.location.latitude, message.location.longitude), language='en')
    address = location.raw.get('address', {})
    city = address.get('city') or address.get('town') or address.get('county') or 'Unknown'
    bot.send_message(message.chat.id, f"You are in {city}")


@bot.message_handler(content_types=["contact"])
def handle_contact(message):
    contact = message.contact
    bot.send_message(message.chat.id, f"Thank you for sharing your contact information, {contact.first_name}.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

def main():
    database = Database(JSONDatabase())
    bot.polling(non_stop=True)

if __name__ == "__main__":
    main()
