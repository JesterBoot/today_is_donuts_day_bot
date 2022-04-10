import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = str(os.getenv('API_TOKEN'))
GROUP_CHAT_ID = int(os.getenv('GROUP_CHAT_ID'))
CHAT_ID = int(os.getenv('CHAT_ID'))
BOT_USERNAME = str(os.getenv('BOT_USERNAME'))
