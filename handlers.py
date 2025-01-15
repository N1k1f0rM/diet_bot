from ftplib import all_errors

import aiohttp
from aiogram import Router
from aiogram.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,
                           MessageAutoDeleteTimerChanged, ReplyKeyboardMarkup, BotCommand, MenuButtonCommands)
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from states import Profile


router = Router()
user_data = {}


@router.message(Command("start"))
async def cmd_nstart(message: Message, state: FSMContext):
    await message.reply("Привет, рады вас видеть, как вас зовут?")
    await state.set_state(Profile.name)


@router.message(Profile.name)
async def process_name(message: Message, state: FSMContext):

    if not message.text.isalpha():
        await message.reply("Пожалуйста, введите корректное имя (только буквы).")
        return

    await state.update_data(name=message.text)

    data_name = await state.get_data()
    nami = data_name.get("name")

    await message.reply(f"Рады вас видеть {nami}! Cколько вам лет? (Введите только число, например 20)")
    await state.set_state(Profile.age)


@router.message(Profile.age)
async def process_age(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.reply("Пожалуйста, введите корректный возраст (только цифры).")
        return

    await state.update_data(age=message.text)
    await message.reply("Какой у вас вес? (Введите только число, например 50)")
    await state.set_state(Profile.weight)


@router.message(Profile.weight)
async def process_age(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.reply("Пожалуйста, введите корректный вес (только цифры).")
        return


    await state.update_data(weight=message.text)
    await message.reply("Какой у вас рост? (Введите только число, например 180)")
    await state.set_state(Profile.height)


@router.message(Profile.height)
async def process_age(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.reply("Пожалуйста, введите корректный рост (только цифры).")
        return


    await state.update_data(height=message.text)
    await message.reply("Сколько часов в день вы двигаетесь? (Введите только число, например 5)")
    await state.set_state(Profile.activity)


@router.message(Profile.activity)
async def process_age(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.reply("Пожалуйста, корректно введите часы (только цифры).")
        return

    await state.update_data(activity=message.text)
    await message.reply("Ваша цель по калориям? Введите только число, например 2400)")
    await state.set_state(Profile.aim)


@router.message(Profile.aim)
async def process_age(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.reply("Пожалуйста, корректно введите калории (только цифры).")
        return

    await state.update_data(aim=message.text)
    await message.reply("Ваш город? Введите название с большой буквы на английском языке")
    await state.set_state(Profile.city)


@router.message(Profile.city)
async def process_city(message: Message, state: FSMContext):

    if not message.text.isalpha():
        await message.reply("Пожалуйста, корректно введите название города.")
        return

    data = await state.get_data()

    name = data.get("name")
    age = data.get("age")
    weight = data.get("weight")
    height = data.get("height")
    activity = data.get("activity")
    aim = data.get("aim")
    city = message.text

    user_data[message.from_user.id] = {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "activity": activity,
        "city": city,
        "aim": aim
    }

    await message.reply(
        f"Спасибо за информацию!\n"
        f"Имя: {name}\n"
        f"Возраст: {age} лет\n"
        f"Вес: {weight} кг\n"
        f"Рост: {height} см\n"
        f"Уровень активности: {activity}\n"
        f"Город: {city}\n"
        f"Цель: {aim}\n"
        f"Всё праивильно?"
    )

    await state.clear()


@router.message(Command("about"))
async def cmd_info(message: Message):
    user_id = message.from_user.id
    user_info = user_data.get(user_id)

    if user_info:
        await message.reply(
            f"Ваши данные:\n"
            f"Имя: {user_info['name']}\n"
            f"Возраст: {user_info['age']} лет\n"
            f"Вес: {user_info['weight']} кг\n"
            f"Рост: {user_info['height']} см\n"
            f"Уровень активности: {user_info['activity']}\n"
            f"Город: {user_info['city']}\n"
            f"Цель: {user_info['aim']}"
        )
    else:
        await message.reply("У вас нет сохраненных данных.")


@router.message(Command("calc_my_norm"))
async def cmd_calc(message: Message):
    if not len(user_data) == 0:
        pass
    else:
        await message.reply("Вы не ввели свои данные!")


@router.message(Command("log_water"))
async def cmd_log_water(message: Message):
    if not len(user_data) == 0:
        pass
    else:
        await message.reply("Вы не ввели свои данные!")


@router.message(Command("log_food"))
async def cmd_log_food(message: Message):
    if not len(user_data) == 0:
        pass
    else:
        await message.reply("Вы не ввели свои данные!")


@router.message(Command("log_workout"))
async def cmd_log_workout(message: Message):
    if not len(user_data) == 0:
        pass
    else:
        await message.reply("Вы не ввели свои данные!")


@router.message(Command("check_progress"))
async def cmd_check_progress(message: Message):
    if not len(user_data) == 0:
        pass
    else:
        await message.reply("Вы не ввели свои данные!")
