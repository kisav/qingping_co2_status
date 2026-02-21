from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from co2_detector import co2_status
from checker import check_status
from models import create_user
from scheduler import scheduler

router = Router()

class Form(StatesGroup):
    APP_KEY_SECRET = State()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет. Я бот. Смирись.")


@router.message(Command("set_key"))
async def set_key(message: Message, state: FSMContext):
    await message.answer("Введите в таком формате: APP_SECRET:APP_KEY")
    await state.set_state(Form.APP_KEY_SECRET)


@router.message(Form.APP_KEY_SECRET)
async def get_key(message: Message, state: FSMContext):
    create_user(message.chat.id, message.text)
    await message.answer('Данные занесены')
    await state.clear()


@router.message(Command("status"))
async def co2_cmd(message: Message):
    level_co2 = co2_status(message.chat.id)
    await message.answer(f"Ваш уровень CO2: {level_co2}")


@router.message(Command("collect"))
async def start_check(message: Message, bot):
    level_co2 = co2_status(message.chat.id)

    scheduler.add_job(
        check_status,
        "interval",
        seconds=10,
        args=(bot, message.chat.id),
        id=f"status_job_{message.chat.id}",
        replace_existing=True
    )

    await message.answer(
        f"Началась постоянная проверка CO2 в комнате. Сейчас {level_co2} ppm!"
    )