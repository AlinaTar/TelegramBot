from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API = '5479875724:AAErX7fJwoSN5Jn_XypOOPI1iE5u_1aC28s'

storage = MemoryStorage()

bot = Bot(token=API)
dp = Dispatcher(bot, storage=storage)
