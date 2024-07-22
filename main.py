from aiogram import types, Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
import asyncio, os

load_dotenv()

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(msg: types.Message) -> None:
    await msg.answer("Привет, мир!")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
