from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Получить фото зверушки'),
            KeyboardButton(text='Начать викторину'),
            KeyboardButton(text='Опекунство')
        ],
        [
            KeyboardButton(text='О нас'),
            KeyboardButton(text='Связаться с нами'),
            KeyboardButton(text='Оставить отзыв'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует?'
)

back_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вернуться назад')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Вернуться назад'
)

start_quiz_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начать'),
            KeyboardButton(text='Вернуться назад'),
        ]
    ],
    resize_keyboard=True,
)
quiz_answers_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='A'),
            KeyboardButton(text='B'),
            KeyboardButton(text='C'),
            KeyboardButton(text='D'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ:'
)
del_kb = ReplyKeyboardRemove()

