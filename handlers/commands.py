import glob
import os
import random

from aiogram import types, Dispatcher
from aiogram.types import InputFile, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot


async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Привет! {message.from_user.first_name}')


async def mem(message: types.Message):
    button_game = InlineKeyboardMarkup(row_width=2)
    button_game.add(InlineKeyboardButton(text="See", callback_data='button_game'))
    await message.answer('If you want random photo click lower: ', reply_markup=button_game)


async def send_mem(call: types.CallbackQuery):
    path = 'media/'
    files = glob.glob(os.path.join(path, "*"))
    random_photo = random.choice(files)
    await bot.send_photo(chat_id=call.from_user.id,
                         photo=InputFile(random_photo))


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_callback_query_handler(send_mem, text='button_game')
