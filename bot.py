import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Online!')


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAOBZFED4pZTH2Hj91QdQ4PqWRsMNQsAAkwAA6_GURo638WRPCyjPy8E')
    await message.answer(
        f"{message.from_user.first_name}, вот список команд, которые я понимаю:\
        \n/logo - показать логотип\n/create_holst - натяжка холста\n/grunt_holst - грунт холста\n/show_picther - показать картины")


@dp.message_handler(content_types=['sticker'])
async def sticker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)


@dp.message_handler(commands=['create_holst'])
async def create_holst(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, как натянуть холст:\n\
    1 - вырезаем холст (размер подрамника + запас на заворот с каждой стороны \n\
    2 - кладём в цент холста с лицевой стороны подрамник и очерчиваем по периметру карандашом \n\
    3 - смачиваем лицевую поверхность холста\n\
    4 - натяжку производим крестом (лево-право, верх-низ)')


@dp.message_handler(commands=['grunt_holst'])
async def grunt_holst(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, как загрунтовать холст:')


@dp.message_handler(commands=['show_picther'])
async def show(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open('Early_autumn.jpg', 'rb'))
    await bot.send_photo(chat_id=message.chat.id, photo=open('Campfire.jpg', 'rb'))


@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open('bot_paint.jpg', 'rb'))


# дописать обработчик
# /qr - создать QR код
# @dp.message_handler(commands=['qr'])
# async def qr(message: types.Message):
#     text = pyqrcode.create(message.text)
#     text.png('code.png', scale=5)
#     await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю(')


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
