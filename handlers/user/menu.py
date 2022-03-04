
from aiogram.types import Message, ReplyKeyboardMarkup
from loader import dp
from filters import IsUser

catalog = '🛍️ Каталог'
balance = '💰 Баланс'
cart = '🛒 Корзина'
delivery_status = '🚚 Статус заказа'

settings = '⚙️ Настройка каталога'
orders = '🚚 Заказы'
questions = '❓ Вопросы'



@dp.message_handler(IsUser(), commands="menu")
async def is_user_menu(message: Message):    
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(catalog)
    markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Меню', reply_markup=markup)