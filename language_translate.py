import logging,time

from aiogram import Bot, Dispatcher, executor, types
from ask import askQuestion
API_TOKEN = ''

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"Hi {user_name}")
    time.sleep(1/50)
    await message.answer("I am a highly intelligent question answering bot")
    time.sleep(1/50)
    await message.answer("Here is an example of asking question:\nQuestion: Where were the 1992 Olympics held?")
    time.sleep(1/100)
    await message.answer("Answer: The 1992 Olympics were held in Barcelona, Spain.")
    time.sleep(3)
    await message.answer("Ask a question now")
    



# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)

#     await message.answer(message.text)

@dp.message_handler()
async def echo(message: types.Message):
    get = askQuestion(message.text)
    await message.answer("I am thinking now ...")
    await message.answer(get)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
