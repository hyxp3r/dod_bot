import asyncio

import aiogram.utils.markdown as md
from aiogram import types, Dispatcher

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from handlers.postgres import write
from handlers.programs import claster
from handlers.operations import getProgram
from create_bot import bot

answers = ["Да", "Нет"]

class Form(StatesGroup):
    start = State()
    name= State()
    answer_1 = State()
    answer_2 = State()
    answer_3 = State()
    answer_4 = State()
    answer_5 = State()
    answer_6 = State()
    answer_7 = State()
    answer_8 = State()

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
markup.add("Да")
markup.add("Нет")
# Старт
#@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):

    await Form.start.set()
    await message.reply("Привет! Рад приветствовать тебя на Дне открытых дверех НГУЭУ! Давай познакомимся поближе, напиши свое имя")
    await Form.next()
"""
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    markup = types.InlineKeyboardMarkup()
    markup.add("/start")

    await state.finish()
    await message.reply('Действие отменено', reply_markup=markup)
"""

async def process_name(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        
        data["name"] = message.text
        data["id"] = message.from_user.id
        data["scoring"] = claster
        data["answers"] = []

    await bot.send_message(
                    message.chat.id,
                    md.text(f'''Приятно познакомиться, <b>{data['name']}</b>!\n\nЯ робот НАРХОЗ. Я создан, чтобы помочь тебе определиться с направлением подготовки, для этого, предлагаю ответить на <b>8</b> вопросов.'''),
                    parse_mode=ParseMode.HTML)
    await bot.send_message(
                message.chat.id,
                md.text(f'''<b>Вопрос 1</b>\nНравится ли тебе заниматься ведением финансового учета?'''),
                parse_mode=ParseMode.HTML, reply_markup=markup)
    await Form.next()

    
async def process_question_1(message: types.Message, state: FSMContext):

    if message.text in answers:
        async with state.proxy() as data:
            
            if message.text in answers:
                data["scoring"]["Экономика и управление"]["score"] += 10
                data["scoring"]["IT"]["score"] += 1

            data["answers"].append(message.text)


        await Form.next()
        
        await bot.send_message(
                message.chat.id,
                md.text(f'''<b>Вопрос 2</b>\nЛюбите ли вы разбирать споры, ссоры между людьми, убеждать, разъяснять?'''),
                parse_mode=ParseMode.HTML, reply_markup=markup)

async def process_question_2(message: types.Message, state: FSMContext):

    if message.text in answers:
        async with state.proxy() as data:

            if message.text == "Да":
                data["scoring"]["Экономика и управление"]["score"] += 0.5
                data["scoring"]["Социально-гуманитарный (иностранные языки)"]["score"] += 0.5
                data["scoring"]["Социально-гуманитарный (сфера анализа данных и PR)"]["score"] += 0.5
                data["scoring"]["Социально-гуманитарный (сфера туризма и гостеприимства)"]["score"] += 0.5
                data["scoring"]["Социально-гуманитарный (психологическое консультирование)"]["score"] += 10
                data["scoring"]["Юридический"]["score"] += 1

            data["answers"].append(message.text)

        await Form.next()
       
        await bot.send_message(
                message.chat.id,
                md.text(f'''<b>Вопрос 3</b>\nНравится ли тебе руководить людьми, друзьями, направлять их усилия для достижения одной общей цели?'''),
                parse_mode=ParseMode.HTML, reply_markup=markup)


async def process_question_3(message: types.Message, state: FSMContext):

    if message.text in answers:
        async with state.proxy() as data:

            if message.text == "Да":
                data["scoring"]["Экономика и управление"]["score"] += 1
                data["scoring"]["Социально-гуманитарный (сфера анализа данных и PR)"]["score"] += 0.5
                data["scoring"]["Социально-гуманитарный (сфера туризма и гостеприимства)"]["score"] += 10
                data["scoring"]["Социально-гуманитарный (психологическое консультирование)"]["score"] += 0.5
                data["scoring"]["Юридический"]["score"] += 1

            data["answers"].append(message.text)

        await Form.next()
       
        await bot.send_message(
        message.chat.id,
        md.text(f'''Супер! Еще немного.\n\n<b>Вопрос 4</b>\nДля тебя интересна «внутренняя» сторона программирования (написание кода, работа со структурой программы и т.д.)?'''),
        parse_mode=ParseMode.HTML, reply_markup=markup)


async def process_question_4(message: types.Message, state: FSMContext):

    if message.text in answers:
        async with state.proxy() as data:
            
            if message.text == "Да":
                data["scoring"]["IT"]["score"] += 20

            data["answers"].append(message.text)

        await Form.next()
       
        await bot.send_message(
        message.chat.id,
        md.text(f'''<b>Вопром 5</b>\nРабота, связанная с цифрами, учетом и контролем, – это довольно скучно. Правда?'''),
        parse_mode=ParseMode.HTML, reply_markup=markup)


async def process_question_5(message: types.Message, state: FSMContext):

    if message.text in answers:
        async with state.proxy() as data:
            
            if message.text == "Да":

                data["scoring"]["Социально-гуманитарный (иностранные языки)"]["score"] += 1
                data["scoring"]["Социально-гуманитарный (сфера анализа данных и PR)"]["score"] += 1
                data["scoring"]["Социально-гуманитарный (сфера туризма и гостеприимства)"]["score"] += 0.5
                data["scoring"]["Социально-гуманитарный (психологическое консультирование)"]["score"] += 1
                data["scoring"]["Социально-гуманитарный (экологический)"]["score"] += 1
                data["scoring"]["Юридический"]["score"] += 10

            data["answers"].append(message.text)

        await Form.next()
       
        await bot.send_message(
        message.chat.id,
        md.text(f'''<b>Вопрос 6</b>\nТебе нравится генерировать новые идеи, заниматься нестандартными задачами?'''),
        parse_mode=ParseMode.HTML, reply_markup=markup)

async def process_question_6(message: types.Message, state: FSMContext):

    if message.text in answers:
        async with state.proxy() as data:
            
            if message.text == "Да":
                data["scoring"]["Экономика и управление"]["score"] += 1
                data["scoring"]["Социально-гуманитарный (сфера анализа данных и PR)"]["score"] += 10
                data["scoring"]["Социально-гуманитарный (сфера туризма и гостеприимства)"]["score"] += 0.5
                data["scoring"]["Социально-гуманитарный (психологическое консультирование)"]["score"] += 1
                data["scoring"]["Социально-гуманитарный (экологический)"]["score"] += 0.5
                data["scoring"]["IT"]["score"] += 0.5
                data["scoring"]["Юридический"]["score"] += 1

            data["answers"].append(message.text)

        await Form.next()
       
        await bot.send_message(
        message.chat.id,
        md.text(f'''<b>Вопрос 7</b>\nНравится ли тебе изучать иностранные языки, интересоавться культурой других стран?'''),
        parse_mode=ParseMode.HTML, reply_markup=markup)


async def process_question_7(message: types.Message, state: FSMContext):

    if message.text in answers:
        async with state.proxy() as data:
            
            if message.text == "Да":
                data["scoring"]["Социально-гуманитарный (иностранные языки)"]["score"] += 10

            data["answers"].append(message.text)

        await Form.next()
       
        await bot.send_message(
        message.chat.id,
        md.text(f'''<b>Вопрос 8</b>\nОтлично! Остался последний вопрос.\nПредпочитаете ли вы наблюдать, изучать экологическую ситуацию в стране?'''),
        parse_mode=ParseMode.HTML, reply_markup=markup)


async def process_question_8(message: types.Message, state: FSMContext):

    if message.text in answers:
        async with state.proxy() as data:
            if message.text == "Да":
                data["scoring"]["Социально-гуманитарный (экологический)"]["score"] += 20

            data["answers"].append(message.text)

                
            data["max_score"] = 0
            data["max_key"] = ""

        await write(data)
        if len(set(data["answers"])) != 1:
            #print(data)
            try:
                data = await getProgram(state)
            except:
                pass

            await bot.send_message(
                                message.chat.id,
                                md.text(f'''Проанализировав ваши ответы, я уверен, что тебе подойдут направления кластера <b>{data["max_key"]}</b>, а именно:\n{data["programs"]}\n\nПредлагаю ознакомиться с ними по подробнее с 13.00 до 14.00 на <b>{data["floor"]}</b> этаже нашего Университета. А если сомневаешься, приходи в ауд. <b>5-213</b> за консультацией приемной комиссии!\n\nЖелаю удачи!'''),
                                parse_mode=ParseMode.HTML)
        else:
                await bot.send_message(
                        message.chat.id,
                        md.text(f'''Мне кажется, что ты еще не определился с выбором карьерного пути.\n\nНичего страшного, выбор действительно сложный! Предлагаю тебе обратиться за индивидуальной консультацией по профориентации в в ауд. <b>5-213</b>, уверен, там тебе помогут сделать верный выбор!\n\nЖелаю удачи!'''),
                        parse_mode=ParseMode.HTML)

        await state.finish()

def register_handlers_client(dp:Dispatcher):

    dp.register_message_handler(cmd_start, commands = ["start"])
    dp.register_message_handler(process_name, state = Form.name)
    dp.register_message_handler(process_question_1, state = Form.answer_1)
    dp.register_message_handler(process_question_2, state = Form.answer_2)
    dp.register_message_handler(process_question_3, state = Form.answer_3)
    dp.register_message_handler(process_question_4, state = Form.answer_4)
    dp.register_message_handler(process_question_5, state = Form.answer_5)
    dp.register_message_handler(process_question_6, state = Form.answer_6)
    dp.register_message_handler(process_question_7, state = Form.answer_7)
    dp.register_message_handler(process_question_8, state = Form.answer_8)





