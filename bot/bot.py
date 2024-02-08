from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, LabeledPrice, Message, PreCheckoutQuery, ContentType, WebAppInfo
from aiogram.dispatcher.filters import Command
from uuid import uuid4
import asyncio

# Bot initialization
bot = Bot(token='6443652897:AAHhUwF8ePz6xaU1SEesSkLN4vwHLiQjJ98')
dp = Dispatcher(bot=bot)

# WebAppInfo setup
web_app = WebAppInfo(url='https://4m00.github.io')

# Reply Keyboard Markup setup
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Купить', web_app=web_app)],
        [KeyboardButton(text='О нас'), KeyboardButton(text='Отзывы')],
        [KeyboardButton(text='Доставка')]
    ],
    resize_keyboard=True
)


# Handlers setup
@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(message.chat.id, 'Добро пожаловать в ElecShop!', reply_markup=keyboard)


PRICE = {
    '1': [LabeledPrice(label='AirPods Pro 2', amount=900000)],
    '2': [LabeledPrice(label='AirPods 3', amount=800000)],
}


@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    product_code = web_app_message.web_app_data.data

    # Get the product name from the PRICE dictionary
    product_name = [price.label for price in PRICE.get(product_code, [])][0]
    # Close the Web App
    await bot.send_message(web_app_message.chat.id, 'Счёт выставлен. Для оплаты используйте форму ниже')
    # Send an invoice
    await bot.send_invoice(web_app_message.chat.id,
                           title=f'{product_name}',
                           description='Описание товара',
                           provider_token='381764678:TEST:76833',
                           currency='rub',
                           need_email=True,
                           need_name=True,
                           need_phone_number=True,
                           need_shipping_address=True,
                           prices=PRICE[web_app_message.web_app_data.data],
                           start_parameter=str(uuid4()),
                           payload=str(uuid4()),
                           )


@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await bot.send_message(message.chat.id, 'Платеж прошел успешно! Заказ оформлен')


@dp.message_handler(lambda message: message.text.lower() == 'отзывы')
async def reviews(message: Message):
    response_text = """
Мы ценим ваше мнение! Если у вас есть отзывы о наших товарах или услугах, пожалуйста, делитесь ими с нами.
Ваши отзывы помогают нам совершенствоваться и предоставлять лучший сервис нашим клиентам.
Спасибо за ваш вклад в нашу работу!
    """
    await bot.send_message(message.chat.id, response_text)


@dp.message_handler(lambda message: message.text.lower() == 'о нас')
async def about_us(message: Message):
    response_text = """
Добро пожаловать в ElecShop - ваш выбор в мире высококачественной электроники!
Мы стремимся предоставить клиентам лучшие продукты и отличный сервис.
Узнайте больше о нашей компании, посетив наш тг канал.
    """
    await bot.send_message(message.chat.id, response_text)


@dp.message_handler(lambda message: message.text.lower() == 'доставка')
async def delivery_info(message: Message):
    response_text = """
Мы гарантируем своевременную и безопасную доставку вашего заказа.
Стоимость доставки рассчитывается в зависимости от вашего местоположения.
Для получения подробной информации о доставке, посетите раздел "Доставка" на нашем сайте.
    """
    await bot.send_message(message.chat.id, response_text)


# Main function
async def main():
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')