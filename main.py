from config import dp, Admins, bot
from aiogram.utils import executor
import logging
from handlers import commands, echo, quiz, FSM_reg
import buttons

async def on_startup(_):
    for id in Admins:
        await bot.send_message(chat_id=id, text='Bot started', reply_markup=buttons.start_buttons)


async def on_shutdown(_):
    for id in Admins:
        await bot.send_message(chat_id=id, text='Bot is off')


commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_reg.register_fsm_for_user(dp)
echo.register_echo(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
