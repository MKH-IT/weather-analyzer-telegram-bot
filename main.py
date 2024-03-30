import telebot
from decouple import config

from database import JSONDatabase, Database
from helpers import gen_languages_markup

TELEGRAM_API_TOKEN = config("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Hello! {message.from_user.first_name}!",
        reply_markup=gen_languages_markup(),
    )
    bot.register_next_step_handler(message, on_click_language)


@bot.callback_query_handler(func=lambda call: call.data.startswith("language_"))
def on_click_language(call):
    if call.data == "language_english":
        bot.answer_callback_query(call.id, "You selected English language.")
    elif call.data == "language_russian":
        bot.answer_callback_query(call.id, "You selected Russian language.")
    elif call.data == "language_uzbek":
        bot.answer_callback_query(call.id, "You selected Uzbek language.")


def main():
    database = Database(JSONDatabase())
    bot.polling(non_stop=True)


if __name__ == "__main__":
    main()
