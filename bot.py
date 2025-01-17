import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, MenuButtonCommands, Message
from aiogram.types.user import User
from aiogram.types.chat import Chat
from config import Secrets
from handlers import router, user_data, cmd_calc
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dateutil import tz


bot = Bot(token=Secrets.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

scheduler = AsyncIOScheduler()

async def send_daily_norms(bott: Bot):
    for user_id in user_data.keys():
        try:
            await bott.send_message(user_id, await cmd_calc(user_id)) # send message
        except Exception as e:
            print(f"Error sending daily norms to user {user_id}: {e}")


scheduler.add_job(send_daily_norms, CronTrigger(hour=0, minute=56, timezone=tz.gettz("Europe/Moscow")))


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
    scheduler.add_job(send_daily_norms, CronTrigger(hour=0, minute=33, timezone=tz.gettz("Europe/Moscow")), args=(bot,))
    await dp.start_polling(bot)
    scheduler.start()


if __name__ == "__main__":
    asyncio.run(main())
