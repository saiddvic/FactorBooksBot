from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db import Product

callback_router = Router()

@callback_router.callback_query(F.data.startswith('category_'))
async def category_handler_callback(callback: CallbackQuery):
    category_id = int(callback.data.split('category_')[-1])
    products = await Product.get_products_by_category_id(category_id)
    ikb = InlineKeyboardBuilder()
    for product in products:

        ikb.add(InlineKeyboardButton(text=product.name, callback_data=f"product_{product.id}"))
    ikb.adjust(2, repeat=True)
    await callback.message.edit_text('📚Productni tanlang', reply_markup=ikb.as_markup())

@callback_router.callback_query(F.data.startswith('product_'))
async def poduct_handler_callback(callback: CallbackQuery):
    product_id = int(callback.data.split('product_')[-1])
    product = await Product.get(product_id)
    await callback.message.delete()
    await callback.message.answer_photo(URLInputFile(product.photo.telegra_image_url), product.name)
    await callback.answer(f"{product_id} tanlandi", show_alert=True)


# async def ikar_handler(query: CallbackQuery):
#     caption = """🔹 Nomi: IKAR to'plami
# "Ikar" to'plami — Usmon Azim: "Bir parcha osmon";
#  Erkin A'zam: "Anoyining jaydari olmasi";
#  Murod Muhammad Do'st: "Galatepaga qaytish";
#  Xurshid Davron: "Samarqand xayoli" kitoblari
# Janri; Adabiy-badiiy,ma'rifiy
# Muqova; Yumshoq
# Kitob haqida;
# 💸 Narxi: 259,000 so'm"""
#     img = URLInputFile('https://telegra.ph/file/367747c429f8993144f86.jpg')
#     ikb = InlineKeyboardBuilder()
#     ikb.add(
#         InlineKeyboardButton(text='➖', callback_data='-1'),
#         InlineKeyboardButton(text='1', callback_data='info'),
#         InlineKeyboardButton(text='➕', callback_data='+1'),
#         InlineKeyboardButton(text='◀️ Orqaga', callback_data='go_back'),
#         InlineKeyboardButton(text="🛒 Savatga qo'shish", callback_data='add'),
#     )
#     ikb.adjust(3, 2, repeat=True)
#     await query.message.answer_photo(img, caption, reply_markup=ikb.as_markup())
#     await query.message.delete()

@callback_router.callback_query(F.data == 'go_back')
async def go_back_handler(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.answer('kategoriyani birini tanlang:')
