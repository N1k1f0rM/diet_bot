import aiohttp
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Profile


router = Router()


user_info = {}


# @router.message(Command("start"))
# async def cmd_start(message: Message):
#     await message.reply("Apple logo")


@router.message(Command("start"))
async def cmd_nstart(message: Message):
    await message.reply("Привет, рады видеть тебя, как тебя зовут?")
    await Profile.name.set()


@router.message(Profile.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.reply("Cколько вам лет?")
    await Profile.age.set()


# @router.message(Command("start"))
# async def cmd_start(message: Message):
#     keyword = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text="Set up account", callback_data="setup")]
#         ]
#     )
#
#     await message.reply("Hello, tell us about")