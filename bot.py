from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import telebot
import pandas as pd

datak = pd.read_excel("clothes.xlsx")
jackets = datak["Jaket"].to_string()
vetrovk = datak["Vetrok"].to_string()
hudi = datak["Hudi"].to_string()
tshirt = datak["Tshirt"].to_string()
data = pd.read_excel("city.xlsx")
cities = data["name"].tolist()
owm = OWM('aa9ed9d25bfe2082ffaa30f78c9b119d')
bot = telebot.TeleBot('1607158305:AAEHgA25jHc1squ5ohh2bja55JN-O8LD1ww')
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "Hi" or message.text == "Hello" or message.text == "/start" or message.text == "привет":
        sti = open('sti.webp', 'rb') ### Изображение приветственного стикера
        bot.send_sticker(message.chat.id, sti) ### отправка приветственного стикера
        bot.send_message(message.chat.id, "Привет, Я - бот который поможет тебе узнать погоду в любом интересующем тебя городе и подобрать соответствующую одежду. Напиши мне название города и погнали. P.S.: Название города надо писать с большой буквы")
    elif message.text in cities: ### Проверка на присутствие города в базе данных
        observation = mgr.weather_at_place(message.text) ### Текст в котором содержится
        w = observation.weather ### Получение погоды в определённом месте
        temp = w.temperature('celsius')["temp"] ### Получение температуры
        if temp < 0 or 0 <= temp <= 5:
            bot.send_message(message.from_user.id, "Температура:" + " " + str(temp) + " " + "по цельсию."  + " К такой погоде как раз подойдёт эта куртка: ")
            bot.send_message(message.from_user.id, jackets[5:])
        elif 5 < temp <= 15:
            bot.send_message(message.from_user.id, "Температура:" + " " + str(temp) + " " + "по цельсию." + " К такой погоде как раз подойдёт эта ветровка: ")
            bot.send_message(message.from_user.id, vetrovk[5:])
        elif 15 < temp <= 21:
            bot.send_message(message.from_user.id, "Температура:" + " " + str(temp) + " " + "по цельсию." + " К такой погоде как раз подойдёт эта кофта: ")
            bot.send_message(message.from_user.id, hudi[5:])
        elif 21 < temp < 100000:
            bot.send_message(message.from_user.id, "Температура:" + " " + str(temp) + " " + "по цельсию." + " К такой погоде как раз подойдут эти футболки: ")
            bot.send_message(message.from_user.id, "К сожалению, футболки пока не доступны(")

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю(. Напиши мне привет")


bot.polling(none_stop=True, interval=0)