from aiogram import Dispatcher, Bot
from decouple import config

Admins = ['1802270883', ]

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)