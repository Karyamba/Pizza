################################  КЛИЕНТСКАЯ ЧАСТЬ  ################################
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db
from aiogram.types import ReplyKeyboardRemove



#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствую Вас', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Tiny_pizza_bot')

#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вс–Чт 10:00 – 22:00, Пт–Сб 10:00 – 00:00')

#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Н. Новгород, ул. Полтавская 22, оф. 210')

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
