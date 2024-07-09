from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


async def quiz(message: types.Message):
    button_quiz = InlineKeyboardMarkup()
    button_quiz_1 = InlineKeyboardButton(text="Next!", callback_data='button_1')
    button_quiz.add(button_quiz_1)

    question = 'BMW or Mercedes?'
    answer = ['BMW', 'Mercedes']

    await bot.send_poll(chat_id=message.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=True,
                        type='quiz',
                        correct_option_id=1,
                        explanation='IZI',
                        open_period=60,
                        reply_markup=button_quiz
                        )


async def quiz_2(call: types.CallbackQuery):
    button_quiz = InlineKeyboardMarkup()
    button_quiz_1 = InlineKeyboardButton(text="Next!", callback_data='button_2')
    button_quiz.add(button_quiz_1)

    question = 'Pizza or Burger?'
    answer = ['Pizza', 'Burger']

    await bot.send_poll(chat_id=call.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=True,
                        type='quiz',
                        correct_option_id=1,
                        explanation='IZI',
                        open_period=60,
                        reply_markup=button_quiz
                        )


async def send_finished(call: types.CallbackQuery):
    with open('media/fd.png', 'rb') as photo:
        await bot.send_photo(chat_id=call.from_user.id, photo=photo)
    await bot.send_message(chat_id=call.from_user.id, text='You are finished')


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1')
    dp.register_callback_query_handler(send_finished, text='button_2')
