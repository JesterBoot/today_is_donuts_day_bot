import logging
import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = str(os.getenv('API_TOKEN'))
GROUP_CHAT_ID = int(os.getenv('GROUP_CHAT_ID'))
CHAT_ID = int(os.getenv('CHAT_ID'))

if not API_TOKEN or not GROUP_CHAT_ID:
    print('Не указан API TOKEN или CHAD ID. Ня, пока!')
    raise SystemExit


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    from handlers import *  # TODO переписать

    executor.start_polling(dp, skip_updates=True)
