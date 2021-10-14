import logging
from keyboard import markup1
from config import TOKEN_API
from get_anekdote import update_url
from aiogram.dispatcher import filters
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет", reply_markup=markup1)

@dp.message_handler(filters.Text(contains='анекдот',ignore_case=True))
async def write_data(message: types.Message):
    await bot.send_message(message.chat.id, update_url())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)