#1375783906:AAHCQISssg50-vrcqxG4SdjIixxXMTA9hL0
import telebot
from covid import Covid
from telebot import types

bot = telebot.TeleBot("1375783906:AAHCQISssg50-vrcqxG4SdjIixxXMTA9hL0")
covid = Covid()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    btn1 = types.KeyboardButton("По всьому світу")
    btn2 = types.KeyboardButton("Russia")
    btn3 = types.KeyboardButton("Ukraine")
    btn4 = types.KeyboardButton("USA")
    markup.add(btn1, btn2, btn3, btn4)

    send_mess = f"<b>Привіт {message.from_user.first_name}!</b>\nОбери країну please."
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "USA":
        location = covid.get_status_by_country_name("us")
    elif get_message_bot == "Ukraine":
        location = covid.get_status_by_country_name("ukraine")
    elif get_message_bot == "Russia":
        location = covid.get_status_by_country_name("russia")
    else:
        confirmed = covid.get_total_confirmed_cases()
        recovered = covid.get_total_recovered()
        deaths = covid.get_total_deaths()
        final_message = f"<u>Данні по всьому світу:</u>\n<b>Хворі: </b>{confirmed}\n" \
                        f"<b>Смертей: </b>{deaths}\n<b>Виздоровили: </b>{recovered}"

    if final_message == "":
        final_message = f"<u>Данні в {get_message_bot}:</u>\n<b>Хворі: </b>{location['confirmed']}\n" \
                        f"<b>Смертей: </b>{location['deaths']}\n<b>Виздоровили: </b>{location['recovered']}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)