import json
import os

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums import ParseMode

# Маршрутизатор
get_animal_router = Router()


# Получаем путь к текущему скрипту
current_dir = os.path.dirname(__file__)
animals_file_path = os.path.join(current_dir, '..', 'picture', 'animals.json')
# Чтение данных о животных из JSON
with open(animals_file_path, 'r', encoding='utf-8') as f:
    animals_data = json.load(f)


# Состояния FSM
class OrderAnimal(StatesGroup):
    waiting_for_name = State()
    waiting_for_next = State()


# Обработчик команды /get_animal
@get_animal_router.message(Command("get_animal"))
async def get_animal(message: types.Message, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Вернуться назад'))
    rep_mark = builder.as_markup(resize_keyboard=True)
    await message.answer('Напиши, какое животное хочешь увидеть:', reply_markup=rep_mark)
    await state.set_state(OrderAnimal.waiting_for_name)


@get_animal_router.message(F.text.lower() == 'вернуться назад')
async def go_back(message: types.Message, state: FSMContext):
    await message.answer("Вы завершили процесс. Если хотите начать снова, используйте команду /get_animal.",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


# Обработчик ввода названия животного
@get_animal_router.message(OrderAnimal.waiting_for_name)
async def process_animal_name(message: types.Message, state: FSMContext):
    animal_name = message.text.strip().title()
    matches = [animal for animal in animals_data if animal_name in animal['title']]
    if matches:
        for animal in matches:
            # Формируем ответ с жирным текстом и ссылкой на фото
            response = f"*{animal['title']}*"
            if animal == matches[-1]:
                response += "\n\nВы можете найти нового животного, просто написав его название в чат."

            # Отправка фото и ответа
            await message.answer_photo(
                photo=animal['image_url'],
                caption=response,
                parse_mode=ParseMode.MARKDOWN,
            )
    else:
        await message.answer("Извините, я не нашел это животное. Попробуйте еще раз.")

    await state.set_state(OrderAnimal.waiting_for_name)
