import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, MenuButtonCommands
from config import Secrets
from handlers import router, cmd_calc
from apscheduler.schedulers.asyncio import AsyncIOScheduler


bot = Bot(token=Secrets.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)
scheduler = AsyncIOScheduler()

scheduler.add_job(cmd_calc, "interval", seconds=15, args=(dp,))


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
    await set_comands(bot)
    await dp.start_polling(bot)
    scheduler.start()


if __name__ == "__main__":
    asyncio.run(main())