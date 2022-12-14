from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '5898593098:AAGTg179orUU4cnveAw1abVViL_n2t2ecPE'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
