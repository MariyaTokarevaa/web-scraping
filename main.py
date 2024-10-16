import requests
from bs4 import BeautifulSoup
import telebot
import random

print ("Бот начал работу")
URL = "https://www.anekdot.ru/release/anekdot/day/"
token = ""
bot = telebot.TeleBot(token)

def parser(URL):
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    anekdots = soup.findAll('div', class_ = 'text')

    return [c.text for c in anekdots]

list_of_anekdots = parser(URL)
random.shuffle(list_of_anekdots)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Добрый день! Чтобы ты не грустил, я расскажу тебе анекдот!"
                                      "Введи любую цифру от 0 до 9")

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.isdigit():
        bot.send_message(message.chat.id, list_of_anekdots[0])
        del list_of_anekdots[0]
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. Ты точно ввел цифру от 0 до 9? Попробуй еще раз")


bot.polling()

