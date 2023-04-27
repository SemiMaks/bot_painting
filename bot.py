import pyqrcode
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply(
        "Список команд, которые я понимаю:\n/logo - показать логотип\n/qr - создать QR код")


@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open('bot_paint.jpg', 'rb'))


# дописать обработчик
@dp.message_handler(commands=['qr'])
async def qr(message: types.Message):
    text = pyqrcode.create(message.text)
    text.png('code.png', scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)


executor.start_polling(dp)
