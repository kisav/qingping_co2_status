import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from co2_detector import co2_status

load_dotenv()


BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет. Я бот. Смирись.")

@dp.message(Command("status"))
async def co2_cmd(message: Message):
    level_co2 = co2_status()

    await message.answer(f"Ваш уровень CO2: {level_co2}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
