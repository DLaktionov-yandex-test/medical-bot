from aiogram import types, Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
import asyncio, os
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards import drug_keyboard


load_dotenv()


bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg:types.Message):
    drugs = ["Кетарол", "Аспирин", "Парацетамол"]
    await msg.answer("Меню лекарств", reply_markup=drug_keyboard(drugs))

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
