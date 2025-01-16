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


class NormalDiet(StatesGroup):
    water_norm = State()
    calories_norm = State()


class Water(StatesGroup):
    volume = State()


class Calories(StatesGroup):
    calorie = State()
