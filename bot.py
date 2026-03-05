import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

user_data = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет 🙌\n\n"
        "Рад, что ты здесь.\n\n"
        "Этот бот создан для глубокой самодиагностики и внутренней работы.\n\n"
        "Но сначала нужно сделать маленький шаг.\n\n"
        "Напиши своё имя."
    )

@dp.message_handler()
async def get_name(message: types.Message):

    user_id = message.from_user.id

    if user_id not in user_data:
        user_data[user_id] = {"name": message.text}
        await message.answer("Спасибо. Теперь отправь свой email.")
        return

    if "email" not in user_data[user_id]:
        user_data[user_id]["email"] = message.text

        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

        keyboard.add("Диагностика стыда")
        keyboard.add("Подарок за подписку")
        keyboard.add("Мои соцсети")
        keyboard.add("Познакомиться ближе")
        keyboard.add("Отзывы клиентов")
        keyboard.add("Личная консультация")

        await message.answer(
            "Спасибо. Ты в главном меню.",
            reply_markup=keyboard
        )

@dp.message_handler(lambda message: message.text == "Личная консультация")
async def consult(message: types.Message):

    await message.answer(
        "Напиши мне в личные сообщения:\n"
        "@IUlashchik"
    )

if __name__ == "__main__":
    executor.start_polling(dp)
