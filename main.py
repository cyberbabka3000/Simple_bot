import telebot
from telebot import types
from which_week import cur_week, cur_week_for_db
from database import get_day_formatting, get_week_formatting

token = '6201059991:AAEoYXDksf4ks9Oc8-awI8ZSXNlaDD_djk0'

bot = telebot.TeleBot(token)

weekday = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг")
    keyboard.row("Пятница", "Суббота", "Эта Неделя", "Следующая неделя")
    keyboard.row("Какая сейчас неделя", "/help")
    bot.send_message(message.chat.id, 'Здравствуйте! Вы что-то хотели?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n'
                                      '1) Выдавать ссылку на наш ВУЗ\n'
                                      '2) Здороваться\n'
                                      '3) Сообщать о расписании на конкретный день, на эту неделю и на следующую неделю\n')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "вуз":
        bot.send_message(message.chat.id, 'О, Вам сюда - https://mtuci.ru/')
    elif message.text.lower() == "какая сейчас неделя":
        bot.send_message(message.chat.id, text=f'На данный момент {cur_week()} неделя')
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет, я Соня, Ваш персональный помощник')
    elif message.text.lower() == "понедельник":
        if cur_week() == "ЧЁТНАЯ":
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(0), 1))}')
        else:
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(1), 1))}')
    elif message.text.lower() == "вторник":
        if cur_week() == "ЧЁТНАЯ":
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(0), 2))}')
        else:
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(1), 2))}')
    elif message.text.lower() == "среду":
        if cur_week() == "ЧЁТНАЯ":
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(0), 3))}')
        else:
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(1), 3))}')
    elif message.text.lower() == "четверг":
        if cur_week() == "ЧЁТНАЯ":
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(0), 4))}')
        else:
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(1), 4))}')
    elif message.text.lower() == "пятницу":
        if cur_week() == "ЧЁТНАЯ":
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(0), 5))}')
        else:
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(1), 5))}')
    elif message.text.lower() == "суббота":
        if cur_week() == "ЧЁТНАЯ":
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(0), 6))}')
        else:
            bot.send_message(message.chat.id, text=f'{(get_day_formatting(cur_week_for_db(1), 6))}')
    elif message.text.lower() == "эта неделя":
        bot.send_message(message.chat.id, text=f'{(get_week_formatting(cur_week_for_db(1)))}')
    elif message.text.lower() == "следующая неделя":
        bot.send_message(message.chat.id, text=f'{(get_week_formatting(cur_week_for_db(0)))}')
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю, напишите "/help", чтобы узнать что я умею')


bot.polling(none_stop=True, interval=0)