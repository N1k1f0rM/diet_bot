import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, MenuButtonCommands, Message
from config import Secrets
from handlers import router, user_data, cmd_calc
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dateutil import tz

bot = Bot(token=Secrets.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)


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


async def send_daily_calculation(bot: Bot, user_data: dict):
    for user_id, user_info in user_data.items():
        message = type('Message', (), {'from_user': type('FromUser', (), {'id': user_id})(), 'chat': type('Chat', (), {'id': user_id})()})
        try:
            await cmd_calc(message)
        except Exception as e:
            print(e)


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_daily_calculation,
        trigger=CronTrigger(hour=23, minute=45, timezone=tz.gettz('Europe/Moscow')),
        kwargs={'bot': bot, 'user_data': user_data}
    )

    scheduler.start()

    await set_comands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())