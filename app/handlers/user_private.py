from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я бот')


@user_private_router.message(Command("about"))
async def start_cmd(message: types.Message):
    await message.answer('Привет, я помощник Московского зоопарка')
