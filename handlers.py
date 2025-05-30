from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Profile, Food, Workout
from back_weather import current_temp
from back_food import get_food_info
from config import info_logger


router = Router()
user_data = {}


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    global user_data
    user_data = {}
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
async def process_weight(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.reply("Пожалуйста, введите корректный вес (только цифры).")
        return


    await state.update_data(weight=message.text)
    await message.reply("Какой у вас рост? (Введите только число, например 180)")
    await state.set_state(Profile.height)


@router.message(Profile.height)
async def process_height(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.reply("Пожалуйста, введите корректный рост (только цифры).")
        return


    await state.update_data(height=message.text)
    await message.reply("Сколько часов в день вы двигаетесь? (Введите только число, например 5)")
    await state.set_state(Profile.activity)


@router.message(Profile.activity)
async def process_activity(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.reply("Пожалуйста, корректно введите часы (только цифры).")
        return

    await state.update_data(activity=message.text)
    await message.reply("Ваша цель по калориям? Введите только число, например 2400)")
    await state.set_state(Profile.aim)


@router.message(Profile.aim)
async def process_aim(message: Message, state: FSMContext):

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
    weather = current_temp(city)

    user_data[message.from_user.id] = {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "activity": activity,
        "city": city,
        "aim": aim,
        "weather": current_temp(city),
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
        f"Погода у вас: {weather}"
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

    user_id = message.from_user.id
    user_info = user_data.get(user_id)

    info_logger.info(f"{user_id} and {user_info}")

    if user_info:
        if current_temp(user_info["city"]) >= 25.0:
            user_info["norm_water"] = int(user_info["weight"]) * 30 + 500 * int(user_info["activity"]) - 1000
        else:
            user_info["norm_water"] = int(user_info["weight"]) * 30 + 500 * int(user_info["activity"])

        user_info["norm_calories"] = 10 * int(user_info["weight"]) + 6.25 * int(user_info["height"]) - 5 * int(user_info["age"])

        await message.reply(
            f"Ваши дневные нормы на сегодня:\n"
            f"Норма воды: {user_info['norm_water']}\n"
            f"Норма калорий: {user_info['norm_calories']}\n"
        )
    else:
        await message.reply("Вы не ввели свои данные!")


@router.message(Command("show_my_norm"))
async def cmd_show_calc(message: Message):
    user_id = message.from_user.id
    user_info = user_data.get(user_id)

    if user_info:
        await message.reply(
            f"На сегодня вам осталось:\n"
            f"Норма воды: {user_info['norm_water']}\n"
            f"Норма калорий: {user_info['norm_calories']}\n")
    else:
        await message.reply("Вы не ввели свои данные!")


@router.message(Command("log_water"))
async def cmd_log_water(message: Message):
    user_id = message.from_user.id
    user_info = user_data.get(user_id)

    if not len(user_data) == 0:
        amount = int(message.text.split()[1])
        user_info["norm_water"] -= int(amount)

        await message.reply(f"Осталось выпить {user_info["norm_water"]}")
    else:
        await message.reply("Вы не ввели свои данные!")


@router.message(Command("log_food"))
async def cmd_log_food(message: Message, state: FSMContext):
    await message.reply("Что вы съели?")
    await state.set_state(Food.food_name)


@router.message(Food.food_name)
async def name_input(message: Message, state: FSMContext):

    await state.update_data(food_name=message.text)
    await message.reply(f"Сколько грамм вы съели?")
    await state.set_state(Food.weight)


@router.message(Food.weight)
async def weight_input(message: Message, state:FSMContext):
    await  state.update_data(weight=message.text)

    user_id = message.from_user.id
    user_info = user_data.get(user_id)

    if user_info:
        data = await state.get_data()

        food_name = data.get('food_name')
        weight = data.get('weight')

        calories = get_food_info(food_name)

        calories_consumed = (calories['calories'] / 100) * float(weight)
        user_info["norm_calories"] -= calories_consumed

        await message.reply(f"Записано: {calories_consumed:.1f} ккал.")
        await state.clear()
    else:
        await message.reply("Произошла ошибка. Попробуйте снова.")


@router.message(Command("log_workout"))
async def cnd_log_workout(message: Message, state: FSMContext):
    await state.set_state(Workout.wotype)
    await message.reply(f"Введите тип тренеровки")


@router.message(Workout.wotype)
async def input_wotype(message: Message, state: FSMContext):
    await state.update_data(wotype=message.text)
    await message.reply(f"Введите продолжительность в минутах")
    await state.set_state(Workout.time)


@router.message(Workout.time)
async def input_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)

    user_id = message.from_user.id
    user_info = user_data.get(user_id)

    data = await state.get_data()
    name = await data.get("wotype")
    timing = float(data.get("time"))

    if user_info:
        user_info["norm_calories"] += 10 * timing
        await message.reply(f"Вы {name} {timing} минут, придётся доесть {10 * timing} калорий")
        await state.clear()
    else:
        await message.reply("Вы не ввели свои данные!")