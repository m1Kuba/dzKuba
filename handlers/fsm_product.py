from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel_markup, start_markup
from aiogram.types import ReplyKeyboardRemove

class FSMProduct(StatesGroup):
    model_name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()

async def start_fsm_product(message: types.Message):
    await message.answer('Введите название модели товара:', reply_markup=cancel_markup)
    await FSMProduct.model_name.set()

async def load_model_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model_name'] = message.text
    await FSMProduct.next()
    await message.answer('Укажите размер товара: ')

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await FSMProduct.next()
    await message.answer('Укажите категорию товара: ')

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await FSMProduct.next()
    await message.answer('Укажите стоимость товара: ')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSMProduct.next()
    await message.answer('Отправьте фотографию товара: ')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await FSMProduct.next()
    await message.answer(f'Верные ли данные?\n'
                         f'Название модели: {data["model_name"]}\n'
                         f'Размер: {data["size"]}\n'
                         f'Категория: {data["category"]}\n'
                         f'Стоимость: {data["price"]} руб.')
    await message.answer_photo(photo=data['photo'])

async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        async with state.proxy() as data:
            # Запись в базу
            await message.answer('Товар добавлен в базу данных!')
            await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('Хорошо, отменено!')
        await state.finish()
    else:
        await message.answer('Введите "Да" или "Нет"!')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=start_markup)

def register_fsm_product_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_fsm_product, commands=['add_product'])
    dp.register_message_handler(load_model_name, state=FSMProduct.model_name)
    dp.register_message_handler(load_size, state=FSMProduct.size)
    dp.register_message_handler(load_category, state=FSMProduct.category)
    dp.register_message_handler(load_price, state=FSMProduct.price)
    dp.register_message_handler(load_photo, state=FSMProduct.photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FSMProduct.submit)
