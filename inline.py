# from aiogram import Bot, types
# from aiogram.utils import executor
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.dispatcher import Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters import Text
#
# storage = MemoryStorage()
#
# TOKEN = '5898593098:AAGTg179orUU4cnveAw1abVViL_n2t2ecPE'
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
# answer = dict()
#
# #Кнопка ссылка
#
# urlkb = InlineKeyboardMarkup(row_width=2)
# urlButton =InlineKeyboardButton(text='Ссылка на youtube', url='https://youtube.com')
# urlButton2 = InlineKeyboardButton(text='Ссылка на гугл',url='https://google.com')
# urlkb.add(urlButton,urlButton2)
#
# @dp.message_handler(commands='ссылка')
# async def url_command(message : types.Message):
#     await message.answer('Ссылочки',reply_markup=urlkb)
#
# inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),
#                                              InlineKeyboardButton(text='NotLike', callback_data='like_-1'))
#
# @dp.message_handler(commands='test')
# async def test_commands(message : types.Message):
#     await message.answer('За видео про деплой бот', reply_markup=inkb)
#
# @dp.callback_query_handler(Text(startswith='like_'))
# async def www_call(callback : types.CallbackQuery):
#     res = int(callback.data.split('_')[1])
#     if f'{callback.from_user.id}' not in answer:
#         answer[f'{callback.from_user.id}'] = res
#         await callback.answer('Вы проголосовали')
#     else:
#         await callback.answer('Вы уже проголосовали',show_alert=True)
#
#     # await callback.answer('Вы проголосовали')
#
#     # await callback.answer('Отлично, теперь еще раз')
#     # await callback.answer('Отлично, теперь еще раз',show_alert=True)
#
#
# executor.start_polling(dp, skip_updates=True)
