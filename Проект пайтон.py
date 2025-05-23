import telebot
from telebot import types

bot = telebot.TeleBot("7717833776:AAHGr_HYEWHPABy87Iin4DIw0gn5V2_oo5A")

ABOUT_MESSAGE = """👋Hi my name Vlados, 15 year's ago 

My device:
Tecno spark go 1 
HONOR 4C 
Siphon 7
Infinix HOT 30I 
Nokia Lumia 830
Phillips Xenium E2101
Mi band 9

My PC:
Intel(R) Pentium(R) 2020M 2.40 GHz
RAM: 4.00 GB
Windows 11 

I'm in:
Spotify: https://open.spotify.com/user/312p56kqhyyoxogimenrg4wexejy?si=qIQnnrCtTseVFXpqO1ENug
Steam:  https://steamcommunity.com/id/Vazilinovoedrislo/
Telegram: @debium
Discord: debium

My project:
My channel in telegram: https://t.me/hakkerchitter
My telegram language beta(TGX, IOS): https://t.me/setlanguage/pluralgram
Useful files: https://t.me/debium_files

Byeeeee👋"""

DONATE_MESSAGE = "https://www.donationalerts.com/r/debium"

@bot.message_handler(commands=['start'])
def send_welcome(message):

    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton('Обо мне', callback_data='about'),
        types.InlineKeyboardButton('Донат', callback_data='donate')
    )
    
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Новость дня")
    btn2 = types.KeyboardButton("Кнопка 2")
    reply_markup.add(btn1, btn2)
    

    bot.send_message(
        message.chat.id,
        "👋 Привет, я бот пользователя @debium. Меня создали на языке Python.\n\n"
        "Нажми на любую кнопку ниже:",
        reply_markup=markup
    )
    

    bot.send_message(
        message.chat.id,
        "Или выберите действие:",
        reply_markup=reply_markup
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'about':
        bot.send_message(call.message.chat.id, ABOUT_MESSAGE)
    elif call.data == 'donate':
        bot.send_message(call.message.chat.id, DONATE_MESSAGE)
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Новость дня":
        bot.send_message(message.chat.id, "Java — 30 лет 23 мая 1995 года состоялся первый выпуск языка программирования Java. Ныне он занимает высокие места в рейтингах популярности среди языков программирования. Первоначальное название Java было Oak (или же Дуб) и его разработка велась с 1991 года. Чуть позже проект был стал называться как Green, а ещё позднее ещё раз переименован — уже в честь сорта кофе из Индонезии. Java изначально был сделан для Star7 — КПК для управления бытовыми устройствами. Только вот Star7, в отличии от его вспомогательного инструмента и языка, не взлетел. Маскот проекта Дюк, изначально присутствовавший в Star7, настолько прижился разработчикам, что его оставили в качестве талисмана для Java. В 1996 году Sun Microsystems представляет первую реализацию для публики — Java 1.0")
    elif message.text == "На всякий она есть":
        bot.send_message(message.chat.id, "Пока что в кнопке нет фунционала")

if __name__ == '__main__':
    print("Бот успешно запущен!")
    bot.polling(none_stop=True)