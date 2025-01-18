import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, MenuButtonCommands
from config import Secrets
from handlers import router
import asyncpg


DATABASE_URL = os.getenv('DATABASE_URL')

bot = Bot(token=Secrets.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def init_db():
    return await asyncpg.connect(DATABASE_URL)


async def set_comands(bots: Bot):
    commands = [
        BotCommand(command="start", description="Начать работу с ботом"),
        BotCommand(command="about", description="Показать информацию о себе"),
        BotCommand(command="calc_my_norm", description="Посчитать мою норму"),
        BotCommand(command="show_my_norm", description="Показать мою норму"),
        BotCommand(command="log_water", description="Внести кол-во выпитой воды"),
        BotCommand(command="log_food", description="Внести еду"),
        BotCommand(command="log_workout", description="Записать тренировку")
    ]

    await bots.set_my_commands(commands)

    menu_buttons = MenuButtonCommands()
    await  bots.set_chat_menu_button(menu_button=menu_buttons)


async def main():
    try:
        await set_comands(bot)
        await dp.start_polling(bot)
        db = await init_db()
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
