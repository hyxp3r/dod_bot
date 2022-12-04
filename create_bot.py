from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

load_dotenv(".env")
bot = Bot(token =  os.environ.get("token"))
token = os.environ.get("token")

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)