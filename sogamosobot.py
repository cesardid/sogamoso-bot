from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint 

button1 = InlineKeyboardButton(text="Random 1-10", callback_data= "Random 1-10")
button2 = InlineKeyboardButton(text="Random 1-100", callback_data= "Random 1-100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)


bot = Bot(token='5909378352:AAFUGuUwRz2xd6VqIvB-9XPA6a-jqQ0gC44')
dp = Dispatcher(bot)

@dp.message_handler(commands=["random"])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)



@dp.message_handler(commands= ["start", "help"])
async def bienvenida(message: types.Message):
    await message.reply("Bienvenido al Bot sobre Sogamoso, en este Bot puedes interactuar por medio del menú de la izquierda de color azul para mirar los lugares turisticos más importantes, como sus historias y sus ubicaciones.")

@dp.callback_query_handler(text= ["Random 1-10", "Random 1-100"])
async def random_value(call: types.CallbackQuery):
    if call.data == "Random 1-10":
        await call.message.answer(randint(1, 10))
    if call.data == "Random 1-100":
        await call.message.answer(randint(1, 100))
    await call.answer()



executor.start_polling(dp)








