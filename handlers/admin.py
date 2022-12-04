from create_bot import bot
from aiogram import types, Dispatcher
import aiogram.utils.markdown as md
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from handlers.postgres import count

admin_sprav = {
    "Дарья Павловна": "smolyakova_darya",
    "Евгений Николаевич": "hyxp3r",
}

admin_kb = InlineKeyboardMarkup(row_width = 1).add(InlineKeyboardButton(text = "Количество использований", callback_data = "count"))
#@dp.message_handler(commands=['start'])
async def admin_start(message: types.Message):

    result = False

    for k, v in admin_sprav.items():

        if message.from_user.username == v:

            name = k
            result = True
            break

    if result:

        await bot.send_message(
                message.chat.id,
                md.text(f'''Добрый день, <b>{name}</b>!\n\nВыберите функцию:'''),
                parse_mode=ParseMode.HTML, reply_markup = admin_kb)
    else:

        await message.reply("Вы не являетесь администратором данного бота.")

#@dp.callback_query_handler(text = "count")
async def count_users(message: types.Message):

    count_text = await count()

    #await callback.message.answer(f"На текущий момент ботом воспользовалось <b>{count_text}</b> абитуриентов!")
    await bot.send_message(
                message.from_user.id,
                md.text(f'''На текущий момент ботом воспользовалось <b>{count_text}</b> абитуриентов!'''),
                parse_mode=ParseMode.HTML)
    





def register_handlers_admin(dp:Dispatcher):

    dp.register_message_handler(admin_start, commands = ["admin"])
    dp.register_callback_query_handler(count_users, text = "count")