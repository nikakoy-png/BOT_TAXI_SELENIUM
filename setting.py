import telebot
from telebot import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

KEY = '5001545541:AAE5xeXN2Y2u-ERKY-5dn9bptE7P0Yw-JcI'

button1 = KeyboardButton('Начать смену')
button2 = KeyboardButton('Закончить смену')

menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    button1, button2
)
