import random
from aiogram import types, Dispatcher
from config import bot

# Список доступных игр
GAMES = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']


async def echo_handler(message: types.Message):
    """Обработчик текстовых сообщений"""
    if 'game' in message.text.lower():
        random_game = random.choice(GAMES)
        await bot.send_dice(chat_id=message.chat.id, emoji=random_game)
    elif message.text.isdigit():
        number = int(message.text)
        await message.answer(number ** 2)
    else:
        try:
            number = float(message.text)
            await message.answer(number ** 2)
        except ValueError:
            await message.answer(message.text)


def register_echo_handlers(dp: Dispatcher):
    """Регистрирует обработчик echo"""
    dp.register_message_handler(echo_handler)
