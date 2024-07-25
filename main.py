# from aiogram import Bot, Dispatcher, types
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.utils import executor
# from fuzzywuzzy import fuzz
# from decouple import config

# API_TOKEN = config('BOT_TOKEN')

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# # Список вопросов и ответов
# qa_pairs = [
#     {"question": "Что такое автокредит?", "answer": "media/chto_takoe_avtokredit.mp4"},
#     {"question": "Кто может получить автокредит?", "answer": "Автокредит предоставляется физическим лицам, индивидуальным предпринимателям."},
#     {"question": "Какая сумма у автокредита?", "answer": "Сумма автокредита от 250 000 сом до 5 000 000 сом."},
#     {"question": "Какой процент автокредита?", "answer": "Процентная ставка автокредита от 23% годовых."},
#     {"question": "Какое целевое назначение у автокредита?", "answer": "Целевое назначение: покупка автотранспорта."},
#     {"question": "Какой первоначальный взнос у автокредита?", "answer": "Первоначальный взнос от 30% от закупочной цены автотранспорта; • При отсутствии собственного вклада допускается предоставление дополнительного залога в виде недвижимости/движимого имущества стоимостью не менее 30% от стоимости приобретаемого автотранспорта."}
# ]

# # Функция для нахождения наиболее подходящего ответа
# def get_best_match(user_question):
#     best_match = {"question": "", "answer": "", "score": 0}
#     for pair in qa_pairs:
#         score = fuzz.ratio(pair["question"].lower(), user_question.lower())
#         if score > best_match["score"]:
#             best_match = {"question": pair["question"], "answer": pair["answer"], "score": score}
#     return best_match if best_match["score"] > 50 else None  # Пороговое значение 50 можно настроить

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(InlineKeyboardButton("Пройти курс", callback_data='course'))
#     keyboard.add(InlineKeyboardButton("Пройти тест", callback_data='test'))

#     await bot.send_message(
#         chat_id=message.chat.id,
#         text="Здравствуйте! Я бот-помощник по кредитам. Задайте мне ваш вопрос.",
#         reply_markup=keyboard
#     )

    
# @dp.message_handler()
# async def handle_question(message: types.Message):
#     user_question = message.text
#     best_match = get_best_match(user_question)
#     if best_match:
#         if best_match["question"] == 'Что такое автокредит?':
#             try:
#                 with open(best_match["answer"], 'rb') as video:
#                     await bot.send_video(message.chat.id, video=video)
#             except FileNotFoundError:
#                 await message.reply("К сожалению, видео не найдено.")
#         else:
#             await message.reply(best_match["answer"])
#     else:
#         await message.reply("Извините, я не могу найти ответ на ваш вопрос.")

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from aiogram.utils import executor
from fuzzywuzzy import fuzz
from decouple import config

API_TOKEN = config('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Список вопросов и ответов
qa_pairs = [
    {"question": "Что такое автокредит?", "answer": "media/chto_takoe_avtokredit.mp4"},
    {"question": "Кто может получить автокредит?", "answer": "Автокредит предоставляется физическим лицам, индивидуальным предпринимателям."},
    {"question": "Какая сумма у автокредита?", "answer": "Сумма автокредита от 250 000 сом до 5 000 000 сом."},
    {"question": "Какой процент автокредита?", "answer": "Процентная ставка автокредита от 23% годовых."},
    {"question": "Какое целевое назначение у автокредита?", "answer": "Целевое назначение: покупка автотранспорта."},
    {"question": "Какой первоначальный взнос у автокредита?", "answer": "Первоначальный взнос от 30% от закупочной цены автотранспорта; • При отсутствии собственного вклада допускается предоставление дополнительного залога в виде недвижимости/движимого имущества стоимостью не менее 30% от стоимости приобретаемого автотранспорта."}
]

# Слайды презентации с текстом
slides = [
    {"image": "media/slide1.png", "text": "Это первый слайд презентации."},
    {"image": "media/slide2.png", "text": "Это второй слайд презентации."},
    {"image": "media/slide3.png", "text": "Это третий слайд презентации."},
    {"image": "media/slide4.png", "text": "Это четвертый слайд презентации."},
    {"image": "media/slide5.png", "text": "Это пятый слайд презентации."},
    {"image": "media/slide6.png", "text": "Это шестой слайд презентации."},
    {"image": "media/slide7.png", "text": "Это седьмой слайд презентации."}
]
current_slide = {}  # хранит текущий слайд для каждого пользователя

def get_best_match(user_question):
    best_match = {"question": "", "answer": "", "score": 0}
    for pair in qa_pairs:
        score = fuzz.ratio(pair["question"].lower(), user_question.lower())
        if score > best_match["score"]:
            best_match = {"question": pair["question"], "answer": pair["answer"], "score": score}
    return best_match if best_match["score"] > 50 else None  # Пороговое значение 50 можно настроить

def get_slide_keyboard(slide_number):
    keyboard = InlineKeyboardMarkup()
    navigation_buttons = []
    if slide_number > 0:
        navigation_buttons.append(InlineKeyboardButton('⬅️ Назад', callback_data=f'prev_{slide_number}'))
    if slide_number < len(slides) - 1:
        navigation_buttons.append(InlineKeyboardButton('Вперед ➡️', callback_data=f'next_{slide_number}'))
    keyboard.row(*navigation_buttons)
    keyboard.add(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return keyboard

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Пройти курс", callback_data='course'))
    keyboard.add(InlineKeyboardButton("Пройти тест", callback_data='test'))

    await bot.send_message(
        chat_id=message.chat.id,
        text="Здравствуйте! Я бот-помощник по кредитам. Задайте мне ваш вопрос.",
        reply_markup=keyboard
    )


@dp.callback_query_handler(lambda c: c.data == 'course')
async def start_presentation(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    current_slide[chat_id] = 0
    slide = slides[current_slide[chat_id]]
    await bot.send_photo(chat_id, 
                         photo=InputFile(slide['image']), 
                         caption=slide['text'], 
                         reply_markup=get_slide_keyboard(0))
    
    
@dp.callback_query_handler(lambda c: c.data == 'home')
async def go_home(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Пройти курс", callback_data='course'))
    keyboard.add(InlineKeyboardButton("Пройти тест", callback_data='test'))
    
    await bot.delete_message(chat_id=chat_id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=chat_id, text="Здравствуйте! Я бот-помощник по кредитам. Задайте мне ваш вопрос.", reply_markup=keyboard)
    

@dp.callback_query_handler(lambda c: c.data.startswith('prev_') or c.data.startswith('next_'))
async def navigate_presentation(callback_query: types.CallbackQuery):
    action, slide_number = callback_query.data.split('_')
    slide_number = int(slide_number)
    chat_id = callback_query.message.chat.id

    if action == 'prev':
        slide_number -= 1
    elif action == 'next':
        slide_number += 1

    current_slide[chat_id] = slide_number
    slide = slides[slide_number]

    # Обновляем изображение
    await bot.edit_message_media(media=types.InputMediaPhoto(InputFile(slide['image'])),
                                 chat_id=chat_id,
                                 message_id=callback_query.message.message_id,
                                 reply_markup=get_slide_keyboard(slide_number))
    
    # Обновляем подпись
    await bot.edit_message_caption(chat_id=chat_id,
                                   message_id=callback_query.message.message_id,
                                   caption=slide['text'],
                                   reply_markup=get_slide_keyboard(slide_number))

@dp.message_handler()
async def handle_question(message: types.Message):
    user_question = message.text
    best_match = get_best_match(user_question)
    if best_match:
        if best_match["question"] == 'Что такое автокредит?':
            try:
                with open(best_match["answer"], 'rb') as video:
                    await bot.send_video(message.chat.id, video=video)
            except FileNotFoundError:
                await message.reply("К сожалению, видео не найдено.")
        else:
            await message.reply(best_match["answer"])
    else:
        await message.reply("Извините, я не могу найти ответ на ваш вопрос.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
