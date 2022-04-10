import logging

from aiogram import Bot, Dispatcher, executor

from settings import API_TOKEN, GROUP_CHAT_ID

if not API_TOKEN or not GROUP_CHAT_ID:
    print('Не указан API TOKEN или GROUP CHAT ID. Ня, пока!')
    raise SystemExit


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    from handlers import *

    loop = asyncio.get_event_loop()
    loop.create_task(name='schedule_message', coro=today_is_donuts_day())
    executor.start_polling(dp, skip_updates=True, loop=loop)
