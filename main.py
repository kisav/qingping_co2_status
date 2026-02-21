import asyncio
from bot_creator import create_bot
from models import init_db
from scheduler import scheduler


async def main():
    init_db()

    bot, dp = create_bot()

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())