import shutil
import time

import requests
import urllib3
from telebot import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from setting import *
from seleniumcontroller import *
from db import *
from bs4 import BeautifulSoup
import glob, os

os.chdir(r"/root/BOT_TAXI_SELENIUM_4/")

db = DB('mongodb://localhost:27017')
bot = Bot(token=KEY)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


def isInt(_str):
    try:
        int(_str)
        return True
    except ValueError:
        return False


@dp.message_handler(commands=['start'])
async def register_point(message):
    await bot.send_message(message.from_user.id, 'Здравствуйте. Я помогу Вам с получением путевых листов КИС АРТ\n'
                                                 'Пожалуйста напишите свой ID водителя КИС АРТ')


async def get_text_massage__(message):
    await bot.send_message(message, 'Ожидайте, мы подготавливаем ваши документы\n')
    time.sleep(5)
    await bot.send_message(message, 'Это займет меньше минуты...\n')
    time.sleep(5)
    await bot.send_message(message, 'Получаем печати...\n')

async def ERROR(message):
    await bot.send_message(message, 'Что то пошло не так.\n')
    await bot.send_message(message, 'Проверьте данные и попробойте позже.\n')

async def ERROR_(message):
    await bot.send_message(message, 'У вас нет путевого листа.\n')

async def send_file(id_user, file):
    await bot.send_message(id_user, 'минуточку...\n', reply_markup=menu)
    uis_pdf = open(r'/root/BOT_TAXI_SELENIUM_4/' + str(file), 'rb')
    await bot.send_document(id_user, uis_pdf)
    uis_pdf.close()
    os.remove(r'/root/BOT_TAXI_SELENIUM_4/' + str(file))


@dp.message_handler(content_types=['text'])
async def get_text_massage(message: types.Message):
    if isInt(message.text):
        id = str(message.text)
        await RegUser(id, message.from_user.id, db,)
        await bot.send_message(message.from_user.id, 'Вы были успешно зарегистрированы в базе\n', reply_markup=menu)

    elif message.text == 'Начать смену':
        name = db.get_user(message.from_user.id)
        await get_text_massage__(message.from_user.id,)
        await getMed(name['fio'], message.from_user.id)


    elif message.text == 'Закончить смену':
        name = db.get_user(message.from_user.id)
        await getAfterTeh(name['fio'], message.from_user.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
