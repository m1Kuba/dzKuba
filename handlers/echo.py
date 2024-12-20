import random
from aiogram import types, Dispatcher
from config import bot

# Список доступных игр
GAMES = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']


async def echo_handler(message: types.Message):
    """Обработчик текстовых сообщений"""
    if 'game' in message.text.lower():  # Проверяем, есть ли слово 'game' в сообщении
        random_game = random.choice(GAMES)  # Выбираем случайную игру
        await bot.send_dice(chat_id=message.chat.id, emoji=random_game)  # Отправляем игру
    elif message.text.isdigit():  # Проверяем, является ли сообщение целым числом
        number = int(message.text)
        await message.answer(number ** 2)  # Возводим в квадрат
    else:
        try:
            # Проверяем, является ли сообщение числом с плавающей точкой
            number = float(message.text)
            await message.answer(number ** 2)  # Возводим в квадрат
        except ValueError:
            # Если сообщение не является числом, повторяем его
            await message.answer(message.text)


def register_echo_handlers(dp: Dispatcher):
    """Регистрирует обработчик echo"""
    dp.register_message_handler(echo_handler)
