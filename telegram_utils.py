import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from co2_detector import co2_status
from checker import check_status
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
load_dotenv()


BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class Form(StatesGroup):
    APP_KEY_SECRET = State()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет. Я бот. Смирись.")

@dp.message(Command("status"))
async def co2_cmd(message: Message):
    level_co2 = co2_status()

    await message.answer(f"Ваш уровень CO2: {level_co2}")

@dp.message(Command("collect"))
async def start_check(message: Message):
    level_co2 = co2_status()
    scheduler.add_job(
        check_status,
        "interval",
        seconds=10,
        args=(bot, message.chat.id),
        id="status_job",
        replace_existing=True
    )
    await message.answer(f"Началась постоянная проверка CO2 в комнате. Сейчас у вас целых {level_co2} ppm!")

@dp.message(Command("set_key"))
async def set_key(message: Message, state:FSMContext):
    await message.answer("Введите в таком формате: APP_SECRET:APP_KEY")
    await state.set_state(Form.APP_KEY_SECRET)

@dp.message(Form.APP_KEY_SECRET)
async def get_key(message: Message, state: FSMContext):
    text = message.text  
    await message.answer(f"Ты ввел: {text}")
    await state.clear()

async def main():
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
