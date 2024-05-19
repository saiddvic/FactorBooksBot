from aiogram import Router, F
from aiogram.types import InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db import Category

inline_router = Router()

@inline_router.message(F.text=="🔵 Biz ijtimoiy tarmoqlarda")
async def social_mediainf_handler(message: Message):
    ikb = InlineKeyboardBuilder()
    ikb.add(
            InlineKeyboardButton(text='IKAR| Factor Books', url='https://t.me/ikar_factor'),
            InlineKeyboardButton(text='Factor Books', url='https://t.me/Factor_books'),
            InlineKeyboardButton(text='"Factor Books" nashriyoti', url='https://t.me/Factorbooks'),
        )
    ikb.adjust(1, repeat=True)
    await message.answer('Biz ijtimoiy tarmoqlarda', reply_markup=ikb.as_markup())


@inline_router.message(F.text == '📚 Kitoblar')
async def books_handler(message: Message):
    categories = await Category.get_all()
    ikb = InlineKeyboardBuilder()
    for category in categories:
        ikb.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    ikb.adjust(2, repeat=True)
    await message.answer('kategoriyani birini tanlang:', reply_markup=ikb.as_markup())
