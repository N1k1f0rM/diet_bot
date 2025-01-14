from aiogram.fsm.state import State, StatesGroup


class Profile(StatesGroup):
    name = State()
    age = State()
    weight = State()
    height = State()
    activity = State()
    city = State()
    aim = State()
