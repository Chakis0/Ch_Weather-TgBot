import telebot
import requests
import json
# import sqlite3

bot = telebot.TeleBot('6229539488:AAHUv2Z8F44TcEUvLNse1LY5h9S9l4pjH0s')
API = '803d06d5de569b324dde5467044fa712'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Температура: {temp} ')

        image = 'img/Sunny.png' if temp > 5.0 else 'img/Sunny-cloudy.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Вы указали не существующий город')


bot.polling(none_stop=True)
