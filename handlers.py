import aiohttp
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.reply("Hello, tell us abouts")


# @router.message(Command("start"))
# async def cmd_start(message: Message):
#     keyword = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text="Set up account", callback_data="setup")]
#         ]
#     )
#
#     await message.reply("Hello, tell us about")