from aiogram import types, executor
from config import bot, dp
import logging
import os


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Твой Telegram ID - {message.from_user.id}')

@dp.message_handler(commands=["mem"])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo, caption='Мемчик')

@dp.message_handler()
async def echo_handler(message: types.Message):
    # Проверяем, является ли сообщение числом
    if message.text.isdigit():  # Для целых чисел
        number = int(message.text)
        await message.answer(number ** 2)
    else:
        try:
            # Для чисел с плавающей точкой
            number = float(message.text)
            await message.answer(number ** 2)
        except ValueError:
            # Если это не число, отправляем сообщение как эхо
            await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)