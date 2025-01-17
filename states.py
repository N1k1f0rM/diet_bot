from aiogram.fsm.state import State, StatesGroup


class Profile(StatesGroup):
    name = State()
    age = State()
    weight = State()
    height = State()
    activity = State()
    city = State()
    aim = State()
    weather = State()
    norm_water = State()
    norm_calories = State()


class Food(StatesGroup):
    food_name = State()
    weight = State()


class Workout(StatesGroup):
    wotype = State()
    wait = State()