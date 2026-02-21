from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router

def create_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    return bot, dp