import asyncio
from aiogram import Bot, Dispatcher
from config import Secrets
from handlers import router, user_data


bot = Bot(token=Secrets.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())