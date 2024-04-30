import os
import asyncio
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from imtihon_db import db_connect, db_cursor
from dotenv import load_dotenv
from keyboard import kb, Ogil_bollar_kiymi, aksesuar, kym_turi, qizlar_kiymi, yupka_razmer, \
    yupka_rangXXS, yupka_rangXS, yupka_rangXL48, yupka_rangX42, yupka_rangL46, yupka_rangM44, \
    yupka_rangXXL49, Tuflik, tuflik, koylak, furbolka, tufli_razmer_gucci, tufli_razmer_loro, \
    tufli_razmer_nike, tufli_razmer_adidas, finkaa, \
    oq_koyle, kepkaa, romoll, loro_37, loro_39, loro_40, loro_38, adidas36, \
    adidas37, adidas39, adidas38, adidas40, nike_36, nike_38, nike_39, nike_37, nike_40, \
    gucci_36, gucci_38, gucci_39, gucci_37, gucci_40, yupka_qora, yupka_pushti, yupka_kok, \
    yupka_yashil, qora_fotbol, oq_futbol, kok_futbol, puwti_futbol, oq_finka, kok_finka, qora_finka, \
    keln_koyle, kepka_oiasi, kepka_ralph, kepka_wollen, kepka_hifiger, romol_kuli, romol_oq, romol_qora, \
    sumka, prada_s, sait_s, alexan_s, monna_s, kurtka, palto, jemper, qiwki_kiym, wm_bronell, \
    wm_polo, wm_zegna, wm_satori, erke_wim, krasof_razmer_loro, krasofka, loro_kras, loro_kras40, \
    loro_kras41, loro_kras42, krasof_razmer_adi, krasof_razmer_gucci, krasof_razmer_nike, adi_kras39, \
    adi_kras41, adi_kras40, adi_kras42, nike_kras39, nike_kras40, nike_kras41, nike_kras42, \
    gucci_kras40, gucci_kras39, gucci_kras41, gucci_kras42, oq_popka, qora_popka, erke_popka, erke_koylela, \
    spotivka, bilio, boss_kids, futbolka_erke, fut_prada, fut_boss, fut_calvin, shortika, moscino, \
    trussardi, kepka_art, erke_kepka, golovni_u, oltn_gerb, caqalo, bodyy, kombezon, qiwki_bola, \
    kuzgi, body, oq_body, sarq_b, qora_b, kok_kombeniz, qora_kombeniz, sarq_kombeniz, kombeniz, \
    kurtka_bola, palto_bola, jumper_bola, qiwki_kiym_bola, kuzgi_kiym_bola, burbery, sandro, tullen

from dllt import Product1, Product2, product4, product3, product5, product6, \
    product7, product8, product9, product10, product11, product12, product13, product15, product14, \
    product16, product17, product18, product19, product20, product21, product22, product23, product24, product25, \
    product26, \
    product27, product28, product29, product30, product31, product32, product34, product35, product36, product37, \
    product33, product38, product39, product40, product41, product42, product43, product44, product45, product46, \
    product47, product48, product49, product50, product51, product52, product53, product54, product55, product56, \
    product57, product58, product59, product60, product61, product62, product63, product64, product65, product66

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from commands import commands

vacancies = {
    'Online Texnika': 'Siz bu yerdan yexnika olish uchun telefon nomer va location yuvorishingiz kerak.',
    'Dokonimiz': 'Dokonimiz Toshkent shahri malika bozori 139B DOKON.',
    'Telefon nomerimiz': 'Bizning dokon telefon nomeri +998937383838.',
    'Dastafka xizmatimiz': 'Dostafka xizmatimizdan foydalanish uchun location jonating',
}

kiyimlar_turi = {'Ortga',
                 'Telefon, -- 500$',
                 'Televizor, -- 200$',
                 'xolodilnik, -- 600$',
                 'Mikro isitgich,  -- 100$',
                 'Gaz plita -- 300$, ',
                 'Konditsoner  -- 400$',
                 }
#
# kiyimlar_turi = {'Ortga',
#                  'Telefon, -- 500$',
#                  'Televizor, -- 200$',
#                  'xolodilnik, -- 600$',
#                  'Mikro isitgich,  -- 100$',
#                  'Gaz plita -- 300$, ',
#                  'Konditsoner  -- 400$',
#                  }
#
# kiyimlar_turi = {'Ortga',
#                  'Telefon, -- 500$',
#                  'Televizor, -- 200$',
#                  'xolodilnik, -- 600$',
#                  'Mikro isitgich,  -- 100$',
#                  'Gaz plita -- 300$, ',
#                  'Konditsoner  -- 400$',
#                  }

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

texnikaa_narxi = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
for nr in kiyimlar_turi:
    texnikaa_narxi.keyboard.append([KeyboardButton(text=nr)])
#
vacancies_keyboard = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
for vacancy in kiyimlar_turi:
    vacancies_keyboard.keyboard.append([KeyboardButton(text=vacancy)])
vacancies_keyboard.keyboard.append([KeyboardButton(text='Back')])

apply_keyboard = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
apply_keyboard.keyboard.append([KeyboardButton(text='Yes'), KeyboardButton(text='No')])

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "⬅️ Ortga")
async def ru_back(message: types.Message):
    await message.answer(
        "Нажмите на Корзину 🛍, чтобы заказать товары или просмотреть их.\n\n", reply_markup=kb)


@dp.message(F.text == "Korzina")
async def show_basket(message: types.Message):
    db_cursor.execute("SELECT * FROM Korzina")
    korzina_items = db_cursor.fetchall()

    if korzina_items:
        response = "Tovar Karzinaga Qoshildi:\n"
        total_price = 0
        for item in korzina_items:
            title = item[1]
            price = item[2]
            quantity = item[3]
            total_price += price * quantity
            response += f"- {title} : {quantity} ta, {price}00 сум\n"
        response += f"Narxi: {round(total_price, 00)}00 сум"
    else:
        response = "Ваша корзина пока пуста."

    await message.answer(response)


@dp.message(F.text == "Sotib Olganlarim")
async def show_basket(message: types.Message):
    db_cursor.execute("SELECT * FROM Buys")
    buys_items = db_cursor.fetchall()
    if buys_items:
        response = "Tovar Sotib olganlarimga Qoshildi:\n"
        total_price = 0
        for item in buys_items:
            title = item[1]
            price = item[2]
            quantity = item[3]
            total_price += price * quantity
            response += f"- {title} : {quantity} ta, {price}00 сум\n"
        response += f"Narxi: {round(total_price, 2)}00 сум"
    else:
        response = "Sotib olganlarim hozircha bosh."

    await message.answer(response)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer_photo(photo=FSInputFile("img_16.png"),
                               caption="Assalomu Aleykum!\n Do'konimizga xush kelibsiz!\n"
                                       "Iltimos ro'yxatdan o'ting /registration"
                                       "Dokonimizdsan turli turdagi mahsulotlarni Ayol, Erkak va Bolalr kiyimini sotib olsangiz boladi\n"
                                       "Hozirda dokonimizda turli Aksiyalar bolib otyapti", reply_markup=kb)


@dp.message(F.text.in_(['Kiyimlar🥻']))
async def cmd_products(message: types.Message):
    await message.answer("Mahsulotlarni boshqarish!", reply_markup=kym_turi)


@dp.message(F.text == 'Aksessuar')
async def cmd_product(message: types.Message):
    await message.answer("Mahsulotlarni boshqarish!", reply_markup=aksesuar)


@dp.message(F.text == 'Ayollar kiyimi👧')
async def cmd_product(message: types.Message):
    await message.answer("Iltimos ozingizga kerakli bolgan \n\n"
                         "yonalishni tanlang!", reply_markup=qizlar_kiymi)


@dp.message(F.text == 'Erkaklar Kiyimi👨')
async def cmd_product(message: types.Message):
    await message.answer("Iltimos ozingizga kerakli bolgan\n\n"
                         "yonalishni tanlang!", reply_markup=Ogil_bollar_kiymi)


#    Yupka

@dp.message(F.text == 'Yupka')
async def cmd_product(message: types.Message):
    await message.answer("Yupka razmerini kiriting📏!", reply_markup=yupka_razmer)


@dp.message(F.text == 'XXS--38')
async def cmd_product(message: types.Message):
    await message.answer("Yupka razmerini kiritildi!"
                         "Iltiomos Yupka rangini kiriting", reply_markup=yupka_rangXXS)


@dp.message(F.text == 'XS--40')
async def cmd_product(message: types.Message):
    await message.answer("Yupka razmerini kiritildi!"
                         "Iltiomos Yupka rangini kiriting", reply_markup=yupka_rangXS)


@dp.message(F.text == 'S--42')
async def cmd_product(message: types.Message):
    await message.answer("Yupka razmerini kiritildi!"
                         "Iltiomos Yupka rangini kiriting", reply_markup=yupka_rangX42)


@dp.message(F.text == 'M--44')
async def cmd_product(message: types.Message):
    await message.answer("Yupka razmerini kiritildi!"
                         "Iltiomos Yupka rangini kiriting", reply_markup=yupka_rangM44)


@dp.message(F.text == 'L--46')
async def cmd_product(message: types.Message):
    await message.answer("Yupka razmerini kiritildi!"
                         "Iltiomos Yupka rangini kiriting", reply_markup=yupka_rangL46)


@dp.message(F.text == 'XL--48')
async def cmd_product(message: types.Message):
    await message.answer("Yupka razmerini kiritildi!"
                         "Iltiomos Yupka rangini kiriting", reply_markup=yupka_rangXL48)


@dp.message(F.text == 'XXL--49')
async def cmd_product(message: types.Message):
    await message.answer("Iltimos!"
                         "Tuflik turini kirgazing!", reply_markup=yupka_rangXXL49)


@dp.message(F.text == 'Krasofka')
async def cmd_product(message: types.Message):
    await message.answer("Krasofka razmerini kiritildi!"
                         "Iltiomos Krasofka razmerini kiriting", reply_markup=krasofka)


@dp.message(F.text == 'Loro Piana-k👟')
async def cmd_product(message: types.Message):
    await message.answer("Tuflik razmerini kiritildi!"
                         "", reply_markup=krasof_razmer_loro)


@dp.message(F.text == "Krasofka-39")
async def send_product_info(message: types.Message):
    messages, photos = Product1.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_kras)


@dp.callback_query(F.data == 'add_korzinka_product51')
async def add_kor(call: types.CallbackQuery):
    print(type(Product1.price))
    print(type(Product1.title))
    print(type(Product1.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Krasofka-39", Product1.price, Product1.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys51')
async def add_kor(call: types.CallbackQuery):
    print(type(Product1.price))
    print(type(Product1.title))
    print(type(Product1.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Krasofka-39", Product1.price, Product1.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Krasofka-40")
async def send_product_info(message: types.Message):
    messages, photos = product35.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_kras40)


@dp.callback_query(F.data == 'add_korzinka_product52')
async def add_kor(call: types.CallbackQuery):
    print(type(product35.price))
    print(type(product35.title))
    print(type(product35.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Krasofka-40", product35.price, product35.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys52')
async def add_kor(call: types.CallbackQuery):
    print(type(product35.price))
    print(type(product35.title))
    print(type(product35.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Krasofka-40", product35.price, product35.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Krasofka-41")
async def send_product_info(message: types.Message):
    messages, photos = product35.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_kras41)


@dp.callback_query(F.data == 'add_korzinka_product53')
async def add_kor(call: types.CallbackQuery):
    print(type(product35.price))
    print(type(product35.title))
    print(type(product35.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Krasofka-41", product35.price, product35.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys53')
async def add_kor(call: types.CallbackQuery):
    print(type(product35.price))
    print(type(product35.title))
    print(type(product35.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Krasofka-41", product35.price, product35.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Krasofka-42")
async def send_product_info(message: types.Message):
    messages, photos = product35.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_kras42)


@dp.callback_query(F.data == 'add_korzinka_product54')
async def add_kor(call: types.CallbackQuery):
    print(type(product35.price))
    print(type(product35.title))
    print(type(product35.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Krasofka-42", product35.price, product35.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys54')
async def add_kor(call: types.CallbackQuery):
    print(type(product35.price))
    print(type(product35.title))
    print(type(product35.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Krasofka-42", product35.price, product35.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Adidas-k👟')
async def cmd_product(message: types.Message):
    await message.answer("Krasofka razmerini kiritildi!"
                         "Iltiomos Krasofka razmerini kiriting", reply_markup=krasof_razmer_adi)


@dp.message(F.text == "Adidas-Krasofka-39")
async def send_product_info(message: types.Message):
    messages, photos = product36.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adi_kras39)


@dp.callback_query(F.data == 'add_korzinka_product55')
async def add_kor(call: types.CallbackQuery):
    print(type(product36.price))
    print(type(product36.title))
    print(type(product36.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-39", product36.price, product36.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys55')
async def add_kor(call: types.CallbackQuery):
    print(type(product36.price))
    print(type(product36.title))
    print(type(product36.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-39", product36.price, product36.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_korzinka_product61')
async def add_kor(call: types.CallbackQuery):
    print(type(product36.price))
    print(type(product36.title))
    print(type(product36.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product36.price, product36.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys61')
async def add_kor(call: types.CallbackQuery):
    print(type(product36.price))
    print(type(product36.title))
    print(type(product36.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product36.price, product36.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Adidas-Krasofka-40")
async def send_product_info(message: types.Message):
    messages, photos = product36.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adi_kras40)


@dp.callback_query(F.data == 'add_korzinka_product56')
async def add_kor(call: types.CallbackQuery):
    print(type(product36.price))
    print(type(product36.title))
    print(type(product36.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-40", product36.price, product36.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys56')
async def add_kor(call: types.CallbackQuery):
    print(type(product36.price))
    print(type(product36.title))
    print(type(product36.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-40", product36.price, product36.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_korzinka_product61')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys61')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Adidas-Krasofka-41")
async def send_product_info(message: types.Message):
    messages, photos = product36.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adi_kras41)


@dp.callback_query(F.data == 'add_korzinka_product57')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys57')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_korzinka_product61')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys61')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Adidas-Krasofka-42")
async def send_product_info(message: types.Message):
    messages, photos = product36.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adi_kras42)


@dp.callback_query(F.data == 'add_korzinka_product58')
async def add_kor(call: types.CallbackQuery):
    print(type(product36.price))
    print(type(product36.title))
    print(type(product36.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-42", product36.price, product36.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys58')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-40", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_korzinka_product61')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys61')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Nike-k👟')
async def cmd_product(message: types.Message):
    await message.answer("Krasofka razmerini kiritildi!\n\n"
                         "Iltiomos Krasofka razmerini kiriting", reply_markup=krasof_razmer_nike)


@dp.message(F.text == "Nike-Krasofka-39")
async def send_product_info(message: types.Message):
    messages, photos = product37.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_kras39)


@dp.callback_query(F.data == 'add_korzinka_product59')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-39", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys59')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-39", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_korzinka_product59')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-39", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys59')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-39", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Nike-Krasofka-40")
async def send_product_info(message: types.Message):
    messages, photos = product37.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_kras40)


@dp.callback_query(F.data == 'add_korzinka_product60')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-40", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys60')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-40", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Nike-Krasofka-41")
async def send_product_info(message: types.Message):
    messages, photos = product37.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_kras41)


@dp.callback_query(F.data == 'add_korzinka_product61')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-41", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys61')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Nike-Krasofka-42")
async def send_product_info(message: types.Message):
    messages, photos = product37.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_kras42)


@dp.callback_query(F.data == 'add_korzinka_product62')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-42", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys62')
async def add_kor(call: types.CallbackQuery):
    print(type(product37.price))
    print(type(product37.title))
    print(type(product37.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-Krasofka-42", product37.price, product37.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Gucci-k👟')
async def cmd_product(message: types.Message):
    await message.answer("Krasofka razmerini kiritildi!"
                         "Iltiomos Krasofka razmerini kiriting", reply_markup=krasof_razmer_gucci)


@dp.message(F.text == "Gucci-Krasofka-39")
async def send_product_info(message: types.Message):
    messages, photos = product38.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_kras39)


@dp.callback_query(F.data == 'add_korzinka_product63')
async def add_kor(call: types.CallbackQuery):
    print(type(product38.price))
    print(type(product38.title))
    print(type(product38.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-Krasofka-39", product38.price, product38.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys63')
async def add_kor(call: types.CallbackQuery):
    print(type(product38.price))
    print(type(product38.title))
    print(type(product38.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-Krasofka-39", product38.price, product38.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Gucci-Krasofka-40")
async def send_product_info(message: types.Message):
    messages, photos = product38.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_kras40)


@dp.callback_query(F.data == 'add_korzinka_product64')
async def add_kor(call: types.CallbackQuery):
    print(type(product38.price))
    print(type(product38.title))
    print(type(product38.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-Krasofka-40", product38.price, product38.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys64')
async def add_kor(call: types.CallbackQuery):
    print(type(product38.price))
    print(type(product38.title))
    print(type(product38.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-Krasofka-40", product38.price, product38.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Gucci-Krasofka-41")
async def send_product_info(message: types.Message):
    messages, photos = product38.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_kras41)


@dp.callback_query(F.data == 'add_korzinka_product65')
async def add_kor(call: types.CallbackQuery):
    print(type(product38.price))
    print(type(product38.title))
    print(type(product38.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-Krasofka-41", product38.price, product38.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys65')
async def add_kor(call: types.CallbackQuery):
    print(type(product38.price))
    print(type(product38.title))
    print(type(product38.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-Krasofka-41", product38.price, product38.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Gucci-Krasofka-42")
async def send_product_info(message: types.Message):
    messages, photos = product38.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_kras42)


@dp.callback_query(F.data == 'add_korzinka_product66')
async def add_kor(call: types.CallbackQuery):
    print(type(product38.price))
    print(type(product38.title))
    print(type(product38.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-Krasofka-42", product38.price, product38.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys66')
async def add_kor(call: types.CallbackQuery):
    print(type(product38.price))
    print(type(product38.title))
    print(type(product38.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-Krasofka-42", product38.price, product38.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Tuflik👢')
async def cmd_product(message: types.Message):
    await message.answer("Yupka razmerini kiritildi!"
                         "Iltiomos Yupka rangini kiriting", reply_markup=Tuflik)


@dp.message(F.text == 'Popka💼')
async def cmd_product(message: types.Message):
    await message.answer("Popka Rangini kiriting!\n\n"
                         "Iltiomos Popka rangini kiriting", reply_markup=erke_popka)


@dp.message(F.text == 'Koylaklar👕')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim turini Tanlang!\n\n"
                         "Iltiomos Koylak turini tanlang", reply_markup=erke_koylela
                         )


@dp.message(F.text == 'Chaqaloqlar Kiyimi👶')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim turini Tanlang!\n\n"
                         "Iltiomos Koylak turini tanlang", reply_markup=caqalo
                         )


@dp.message(F.text == 'Body')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim turini Tanlang!\n\n"
                         "Iltiomos Koylak turini tanlang", reply_markup=body
                         )


@dp.message(F.text == 'Kombenizon')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim turini Tanlang!\n\n"
                         "Iltiomos Koylak turini tanlang", reply_markup=kombeniz
                         )


@dp.message(F.text == "Sariq")
async def send_product_info(message: types.Message):
    messages, photos = product57.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=sarq_kombeniz)


@dp.callback_query(F.data == 'add_korzinka_product86')
async def add_kor(call: types.CallbackQuery):
    print(type(product57.price))
    print(type(product57.title))
    print(type(product57.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Sariq", product57.price, product57.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys86')
async def add_kor(call: types.CallbackQuery):
    print(type(product57.price))
    print(type(product57.title))
    print(type(product57.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Sariq", product57.price, product57.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Kok")
async def send_product_info(message: types.Message):
    messages, photos = product58.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kok_kombeniz)


@dp.callback_query(F.data == 'add_korzinka_product87')
async def add_kor(call: types.CallbackQuery):
    print(type(product58.price))
    print(type(product58.title))
    print(type(product58.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kok", product58.price, product58.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys87')
async def add_kor(call: types.CallbackQuery):
    print(type(product58.price))
    print(type(product58.title))
    print(type(product58.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kok", product58.price, product58.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Qora")
async def send_product_info(message: types.Message):
    messages, photos = product59.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=qora_kombeniz)


@dp.callback_query(F.data == 'add_korzinka_product88')
async def add_kor(call: types.CallbackQuery):
    print(type(product59.price))
    print(type(product59.title))
    print(type(product59.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora", product59.price, product59.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys88')
async def add_kor(call: types.CallbackQuery):
    print(type(product59.price))
    print(type(product59.title))
    print(type(product59.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora", product59.price, product59.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Oq")
async def send_product_info(message: types.Message):
    messages, photos = product54.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=oq_body)


@dp.callback_query(F.data == 'add_korzinka_product83')
async def add_kor(call: types.CallbackQuery):
    print(type(product54.price))
    print(type(product54.title))
    print(type(product54.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oq", product54.price, product54.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys83')
async def add_kor(call: types.CallbackQuery):
    print(type(product54.price))
    print(type(product54.title))
    print(type(product54.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oq", product54.price, product54.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Sariq")
async def send_product_info(message: types.Message):
    messages, photos = product55.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=sarq_b)


@dp.callback_query(F.data == 'add_korzinka_product84')
async def add_kor(call: types.CallbackQuery):
    print(type(product55.price))
    print(type(product55.title))
    print(type(product55.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Sariq", product55.price, product55.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys84')
async def add_kor(call: types.CallbackQuery):
    print(type(product55.price))
    print(type(product55.title))
    print(type(product55.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Sariq", product55.price, product55.quantity))
    db_connect.commit()
    await call.answer("Product added!")


### Xato borrrrrrrrrrrrrrrrrrrrr

@dp.message(F.text == "Qora")
async def send_product_info(message: types.Message):
    messages, photos = product56.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=qora_b)


@dp.callback_query(F.data == 'add_korzinka_product85')
async def add_kor(call: types.CallbackQuery):
    print(type(product56.price))
    print(type(product56.title))
    print(type(product56.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora", product56.price, product56.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys85')
async def add_kor(call: types.CallbackQuery):
    print(type(product56.price))
    print(type(product56.title))
    print(type(product56.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora", product56.price, product56.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Spartivka')
async def cmd_product(message: types.Message):
    await message.answer("Spartivka turini Tanlang!\n\n"
                         "Iltiomos Spartivka turini tanlang", reply_markup=spotivka
                         )


@dp.message(F.text == "Boss Kidswear")
async def send_product_info(message: types.Message):
    messages, photos = product41.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=boss_kids)


@dp.callback_query(F.data == 'add_korzinka_product69')
async def add_kor(call: types.CallbackQuery):
    print(type(product41.price))
    print(type(product41.title))
    print(type(product41.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Boss Kidswear", product41.price, product41.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys69')
async def add_kor(call: types.CallbackQuery):
    print(type(product41.price))
    print(type(product41.title))
    print(type(product41.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Boss Kidswear", product41.price, product41.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Billionarie")
async def send_product_info(message: types.Message):
    messages, photos = product42.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=bilio)


@dp.callback_query(F.data == 'add_korzinka_product70')
async def add_kor(call: types.CallbackQuery):
    print(type(product42.price))
    print(type(product42.title))
    print(type(product42.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Billionarie", product42.price, product42.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys70')
async def add_kor(call: types.CallbackQuery):
    print(type(product42.price))
    print(type(product42.title))
    print(type(product42.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Billionarie", product42.price, product42.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Shortik')
async def cmd_product(message: types.Message):
    await message.answer("Shortik turini kiritildi!"
                         "", reply_markup=shortika)


@dp.message(F.text == "Moschino")
async def send_product_info(message: types.Message):
    messages, photos = product46.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=moscino)


@dp.callback_query(F.data == 'add_korzinka_product74')
async def add_kor(call: types.CallbackQuery):
    print(type(product46.price))
    print(type(product46.title))
    print(type(product46.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Moschino", product46.price, product46.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys74')
async def add_kor(call: types.CallbackQuery):
    print(type(product46.price))
    print(type(product46.title))
    print(type(product46.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Moschino", product46.price, product46.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Trussardi")
async def send_product_info(message: types.Message):
    messages, photos = product47.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=trussardi)


@dp.callback_query(F.data == 'add_korzinka_product75')
async def add_kor(call: types.CallbackQuery):
    print(type(product47.price))
    print(type(product47.title))
    print(type(product47.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Trussardi", product47.price, product47.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys75')
async def add_kor(call: types.CallbackQuery):
    print(type(product47.price))
    print(type(product47.title))
    print(type(product47.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Trussardi", product47.price, product47.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Futbolka')
async def cmd_product(message: types.Message):
    await message.answer("Tuflik razmerini kiritildi!"
                         "", reply_markup=futbolka_erke)


@dp.message(F.text == 'Kepkalar🎓')
async def cmd_product(message: types.Message):
    await message.answer("Iltimos Kepka turini kiriting!"
                         "", reply_markup=erke_kepka)


@dp.message(F.text == "Oltin Gerbi")
async def send_product_info(message: types.Message):
    messages, photos = product48.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=oltn_gerb)


@dp.callback_query(F.data == 'add_korzinka_product76')
async def add_kor(call: types.CallbackQuery):
    print(type(product48.price))
    print(type(product48.title))
    print(type(product48.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oltin Gerbi", product48.price, product48.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys76')
async def add_kor(call: types.CallbackQuery):
    print(type(product48.price))
    print(type(product48.title))
    print(type(product48.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oltin Gerbi", product48.price, product48.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Kepka-Art")
async def send_product_info(message: types.Message):
    messages, photos = product49.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kepka_art)


@dp.callback_query(F.data == 'add_korzinka_product77')
async def add_kor(call: types.CallbackQuery):
    print(type(product49.price))
    print(type(product49.title))
    print(type(product49.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kepka-Art", product49.price, product49.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys77')
async def add_kor(call: types.CallbackQuery):
    print(type(product49.price))
    print(type(product49.title))
    print(type(product49.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kepka-Art", product49.price, product49.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Golovnie ubori")
async def send_product_info(message: types.Message):
    messages, photos = product50.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=golovni_u)


@dp.callback_query(F.data == 'add_korzinka_product78')
async def add_kor(call: types.CallbackQuery):
    print(type(product50.price))
    print(type(product50.title))
    print(type(product50.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Golovnie ubori", product50.price, product50.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys77')
async def add_kor(call: types.CallbackQuery):
    print(type(product50.price))
    print(type(product50.title))
    print(type(product50.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Golovnie ubori", product50.price, product50.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Prada")
async def send_product_info(message: types.Message):
    messages, photos = product43.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=fut_prada)


@dp.callback_query(F.data == 'add_korzinka_product71')
async def add_kor(call: types.CallbackQuery):
    print(type(product43.price))
    print(type(product43.title))
    print(type(product43.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Prada", product43.price, product43.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys71')
async def add_kor(call: types.CallbackQuery):
    print(type(product43.price))
    print(type(product43.title))
    print(type(product43.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Prada", product43.price, product43.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Calvin")
async def send_product_info(message: types.Message):
    messages, photos = product44.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=fut_calvin)


@dp.callback_query(F.data == 'add_korzinka_product72')
async def add_kor(call: types.CallbackQuery):
    print(type(product44.price))
    print(type(product44.title))
    print(type(product44.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Calvin", product44.price, product44.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys72')
async def add_kor(call: types.CallbackQuery):
    print(type(product44.price))
    print(type(product44.title))
    print(type(product44.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Calvin", product44.price, product44.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Boss")
async def send_product_info(message: types.Message):
    messages, photos = product45.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=fut_boss)


@dp.callback_query(F.data == 'add_korzinka_product73')
async def add_kor(call: types.CallbackQuery):
    print(type(product45.price))
    print(type(product45.title))
    print(type(product45.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Boss", product45.price, product45.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys73')
async def add_kor(call: types.CallbackQuery):
    print(type(product45.price))
    print(type(product45.title))
    print(type(product45.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Boss", product44.price, product44.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Oq Popka")
async def send_product_info(message: types.Message):
    messages, photos = product39.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=oq_popka)


@dp.callback_query(F.data == 'add_korzinka_product67')
async def add_kor(call: types.CallbackQuery):
    print(type(product39.price))
    print(type(product39.title))
    print(type(product39.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oq Popka", product39.price, product39.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys67')
async def add_kor(call: types.CallbackQuery):
    print(type(product39.price))
    print(type(product39.title))
    print(type(product39.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oq Popka", product39.price, product39.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Qora Popka")
async def send_product_info(message: types.Message):
    messages, photos = product40.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=qora_popka)


@dp.callback_query(F.data == 'add_korzinka_product68')
async def add_kor(call: types.CallbackQuery):
    print(type(product40.price))
    print(type(product40.title))
    print(type(product40.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora Popka", product40.price, product40.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys68')
async def add_kor(call: types.CallbackQuery):
    print(type(product40.price))
    print(type(product40.title))
    print(type(product40.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora Popka", product40.price, product40.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Loro Piana👟')
async def cmd_product(message: types.Message):
    await message.answer("Tuflik razmerini kiritildi!"
                         "", reply_markup=tufli_razmer_loro)


@dp.message(F.text == "Loro-36")
async def send_product_info(message: types.Message):
    messages, photos = Product1.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_37)


@dp.callback_query(F.data == 'add_korzinka_product1')
async def add_kor(call: types.CallbackQuery):
    print(type(Product1.price))
    print(type(Product1.title))
    print(type(Product1.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-36", Product1.price, Product1.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys1')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-36", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Loro-37")
async def send_product_info(message: types.Message):
    messages, photos = Product1.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_37)


@dp.callback_query(F.data == 'add_korzinka_product2')
async def add_kor(call: types.CallbackQuery):
    print(type(Product1.price))
    print(type(Product1.title))
    print(type(Product1.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-37", Product1.price, Product1.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys2')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-37", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Loro-38")
async def send_product_info(message: types.Message):
    messages, photos = Product1.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_38)


@dp.callback_query(F.data == 'add_korzinka_product3')
async def add_kor(call: types.CallbackQuery):
    print(type(Product1.price))
    print(type(Product1.title))
    print(type(Product1.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-38", Product1.price, Product1.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys3')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-38", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Loro-39")
async def send_product_info(message: types.Message):
    messages, photos = Product1.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_39)


@dp.callback_query(F.data == 'add_korzinka_product4')
async def add_kor(call: types.CallbackQuery):
    print(type(Product1.price))
    print(type(Product1.title))
    print(type(Product1.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-39", Product1.price, Product1.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys4')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-39", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Loro-40")
async def send_product_info(message: types.Message):
    messages, photos = Product1.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=loro_40)


@dp.callback_query(F.data == 'add_korzinka_product5')
async def add_kor(call: types.CallbackQuery):
    print(type(Product1.price))
    print(type(Product1.title))
    print(type(Product1.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-40", Product1.price, Product1.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys5')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Loro-40", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Adidas👟')
async def cmd_product(message: types.Message):
    await message.answer("Tuflik razmerini kiritildi!"
                         "", reply_markup=tufli_razmer_adidas)


@dp.message(F.text == "Adidas-36")
async def send_product_info(message: types.Message):
    messages, photos = Product2.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adidas36)


@dp.callback_query(F.data == 'add_korzinka_product6')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-36", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys6')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-36", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Adidas-37")
async def send_product_info(message: types.Message):
    messages, photos = Product2.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adidas37)


@dp.callback_query(F.data == 'add_korzinka_product7')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-37", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys7')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-37", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Adidas-38")
async def send_product_info(message: types.Message):
    messages, photos = Product2.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adidas38)


@dp.callback_query(F.data == 'add_korzinka_product8')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-38", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys8')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-38", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Adidas-39")
async def send_product_info(message: types.Message):
    messages, photos = Product2.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adidas39)


@dp.callback_query(F.data == 'add_korzinka_product9')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-39", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys9')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-39", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Adidas-40")
async def send_product_info(message: types.Message):
    messages, photos = Product2.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=adidas40)


@dp.callback_query(F.data == 'add_korzinka_product10')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-40", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys10')
async def add_kor(call: types.CallbackQuery):
    print(type(Product2.price))
    print(type(Product2.title))
    print(type(Product2.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Adidas-40", Product2.price, Product2.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Nike👟')
async def cmd_product(message: types.Message):
    await message.answer("Tuflik razmerini kiritildi!"
                         "", reply_markup=tufli_razmer_nike)


@dp.message(F.text == "Nike-36")
async def send_product_info(message: types.Message):
    messages, photos = product3.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_36)


@dp.callback_query(F.data == 'add_korzinka_product11')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-36", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys11')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-36", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Nike-37")
async def send_product_info(message: types.Message):
    messages, photos = product3.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_37)


@dp.callback_query(F.data == 'add_korzinka_product12')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-37", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys12')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-37", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Nike-38")
async def send_product_info(message: types.Message):
    messages, photos = product3.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_38)


@dp.callback_query(F.data == 'add_korzinka_product13')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-38", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys13')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-38", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Nike-39")
async def send_product_info(message: types.Message):
    messages, photos = product3.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_39)


@dp.callback_query(F.data == 'add_korzinka_product14')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-39", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys14')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-39", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Nike-40")
async def send_product_info(message: types.Message):
    messages, photos = product3.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=nike_40)


@dp.callback_query(F.data == 'add_korzinka_product15')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-40", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys15')
async def add_kor(call: types.CallbackQuery):
    print(type(product3.price))
    print(type(product3.title))
    print(type(product3.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Nike-40", product3.price, product3.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Gucci👟')
async def cmd_product(message: types.Message):
    await message.answer("Tuflik razmerini kiritildi!"
                         "", reply_markup=tufli_razmer_gucci)


@dp.message(F.text == "Gucci-36")
async def send_product_info(message: types.Message):
    messages, photos = product4.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_36)


@dp.callback_query(F.data == 'add_korzinka_product16')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-36", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys16')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-36", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Gucci-37")
async def send_product_info(message: types.Message):
    messages, photos = product4.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_37)


@dp.callback_query(F.data == 'add_korzinka_product17')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-37", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys17')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-37", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Gucci-38")
async def send_product_info(message: types.Message):
    messages, photos = product4.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_38)


@dp.callback_query(F.data == 'add_korzinka_product18')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-38", product4.price, product5.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys18')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-38", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Gucci-39")
async def send_product_info(message: types.Message):
    messages, photos = product4.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_39)


@dp.callback_query(F.data == 'add_korzinka_product19')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-39", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys19')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-39", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Gucci-40")
async def send_product_info(message: types.Message):
    messages, photos = product4.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=gucci_40)


@dp.callback_query(F.data == 'add_korzinka_product20')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-40", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys20')
async def add_kor(call: types.CallbackQuery):
    print(type(product4.price))
    print(type(product4.title))
    print(type(product4.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-40", product4.price, product4.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Gucci-40")
async def send_product_info(message: types.Message):
    messages, photos = product4.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=tuflik)


# @dp.message(F.text == "36")
# async def send_product_info(message: types.Message):
#     messages, photos = product4.send_product_info()
#     print(photos)
#     await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=tuflik)
#
#
# @dp.message(F.text == "37")
# async def send_product_info(message: types.Message):
#     messages, photos = product4.send_product_info()
#     print(photos)
#     await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=tuflik)
#
#
# @dp.message(F.text == "38")
# async def send_product_info(message: types.Message):
#     messages, photos = product4.send_product_info()
#     print(photos)
#     await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=tuflik)
#
#
# @dp.message(F.text == "39")
# async def send_product_info(message: types.Message):
#     messages, photos = product4.send_product_info()
#     print(photos)
#     await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=tuflik)
#
#
# @dp.message(F.text == "40")
# async def send_product_info(message: types.Message):
#     messages, photos = product4.send_product_info()
#     print(photos)
#     await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=tuflik)
#

@dp.message(F.text == "Qora⚫")
async def send_product_info(message: types.Message):
    messages, photos = product5.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=yupka_qora)


@dp.callback_query(F.data == 'add_korzinka_product21')
async def add_kor(call: types.CallbackQuery):
    print(type(product5.price))
    print(type(product5.title))
    print(type(product5.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora⚫", product5.price, product5.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys21')
async def add_kor(call: types.CallbackQuery):
    print(type(product5.price))
    print(type(product5.title))
    print(type(product5.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora⚫", product5.price, product5.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Kok🔵")
async def send_product_info(message: types.Message):
    messages, photos = product6.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=yupka_kok)


@dp.callback_query(F.data == 'add_korzinka_product22')
async def add_kor(call: types.CallbackQuery):
    print(type(product6.price))
    print(type(product6.title))
    print(type(product6.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kok🔵", product6.price, product6.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys22')
async def add_kor(call: types.CallbackQuery):
    print(type(product6.price))
    print(type(product6.title))
    print(type(product6.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kok🔵", product6.price, product6.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Pushti🩷")
async def send_product_info(message: types.Message):
    messages, photos = product7.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=yupka_pushti)  #


@dp.callback_query(F.data == 'add_korzinka_product23')
async def add_kor(call: types.CallbackQuery):
    print(type(product7.price))
    print(type(product7.title))
    print(type(product7.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Pushti🩷", product7.price, product7.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys23')
async def add_kor(call: types.CallbackQuery):
    print(type(product7.price))
    print(type(product7.title))
    print(type(product7.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Pushti🩷", product7.price, product7.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Yashil🟢")
async def send_product_info(message: types.Message):
    messages, photos = product8.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=yupka_yashil)


@dp.callback_query(F.data == 'add_korzinka_product24')
async def add_kor(call: types.CallbackQuery):
    print(type(product8.price))
    print(type(product8.title))
    print(type(product8.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Yashil🟢", product8.price, product8.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys24')
async def add_kor(call: types.CallbackQuery):
    print(type(product8.price))
    print(type(product8.title))
    print(type(product8.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Yashil🟢", product8.price, product8.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Koylak👕')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim turini kirgazing!"
                         "", reply_markup=koylak)


@dp.message(F.text == 'Futbolka👕')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim rangini tanlang!"
                         "", reply_markup=furbolka)


@dp.message(F.text == "Koylak👕")
async def send_product_info(message: types.Message):
    messages, photos = product8.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=koylak)


@dp.message(F.text == "Qora rangli⚫")
async def send_product_info(message: types.Message):
    messages, photos = product9.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=qora_fotbol)


@dp.callback_query(F.data == 'add_korzinka_product25')
async def add_kor(call: types.CallbackQuery):
    print(type(product9.price))
    print(type(product9.title))
    print(type(product9.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora rangli⚫", product9.price, product9.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys25')
async def add_kor(call: types.CallbackQuery):
    print(type(product9.price))
    print(type(product9.title))
    print(type(product9.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora rangli⚫", product9.price, product9.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Kok rangli🔵")
async def send_product_info(message: types.Message):
    messages, photos = product10.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kok_futbol)


@dp.callback_query(F.data == 'add_korzinka_product26')
async def add_kor(call: types.CallbackQuery):
    print(type(product10.price))
    print(type(product10.title))
    print(type(product10.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kok rangli🔵", product10.price, product10.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys26')
async def add_kor(call: types.CallbackQuery):
    print(type(product10.price))
    print(type(product10.title))
    print(type(product10.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Gucci-40", product10.price, product10.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Oq rangli⚪")
async def send_product_info(message: types.Message):
    messages, photos = product11.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=oq_futbol)


@dp.callback_query(F.data == 'add_korzinka_product27')
async def add_kor(call: types.CallbackQuery):
    print(type(product11.price))
    print(type(product11.title))
    print(type(product11.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oq rangli⚪", product11.price, product11.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys27')
async def add_kor(call: types.CallbackQuery):
    print(type(product11.price))
    print(type(product11.title))
    print(type(product11.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oq rangli⚪", product11.price, product11.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Pushti rangli🩷")
async def send_product_info(message: types.Message):
    messages, photos = product12.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=puwti_futbol)


@dp.callback_query(F.data == 'add_korzinka_product28')
async def add_kor(call: types.CallbackQuery):
    print(type(product12.price))
    print(type(product12.title))
    print(type(product12.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Pushti rangli🩷", product12.price, product12.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys28')
async def add_kor(call: types.CallbackQuery):
    print(type(product12.price))
    print(type(product12.title))
    print(type(product12.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Pushti rangli🩷", product12.price, product12.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Finka')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim turini kirgazing!"
                         "", reply_markup=finkaa)


@dp.message(F.text == "Qora Rangli⚫")
async def send_product_info(message: types.Message):
    messages, photos = product13.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=qora_finka)


@dp.callback_query(F.data == 'add_korzinka_product29')
async def add_kor(call: types.CallbackQuery):
    print(type(product13.price))
    print(type(product13.title))
    print(type(product13.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora Rangli⚫", product13.price, product13.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys29')
async def add_kor(call: types.CallbackQuery):
    print(type(product13.price))
    print(type(product13.title))
    print(type(product13.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Qora Rangli⚫", product13.price, product13.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Oq Rangli⚪")
async def send_product_info(message: types.Message):
    messages, photos = product15.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=oq_finka)


@dp.callback_query(F.data == 'add_korzinka_product30')
async def add_kor(call: types.CallbackQuery):
    print(type(product15.price))
    print(type(product15.title))
    print(type(product15.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oq Rangli⚪", product15.price, product15.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys30')
async def add_kor(call: types.CallbackQuery):
    print(type(product15.price))
    print(type(product15.title))
    print(type(product15.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Oq Rangli⚪", product15.price, product15.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Kok Rangli🔵")
async def send_product_info(message: types.Message):
    messages, photos = product14.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kok_finka)


@dp.callback_query(F.data == 'add_korzinka_product31')
async def add_kor(call: types.CallbackQuery):
    print(type(product14.price))
    print(type(product14.title))
    print(type(product14.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kok Rangli🔵", product14.price, product14.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys31')
async def add_kor(call: types.CallbackQuery):
    print(type(product14.price))
    print(type(product14.title))
    print(type(product14.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kok Rangli🔵", product14.price, product14.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Oq Koylak⚪')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim turini kirgazing!"
                         "", reply_markup=oq_koyle)


@dp.message(F.text == 'Kepka🎓')
async def cmd_product(message: types.Message):
    await message.answer("Kepka turini kirgazing!"
                         "", reply_markup=kepkaa)


@dp.message(F.text == "Kenlin Koylak")
async def send_product_info(message: types.Message):
    messages, photos = product16.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=keln_koyle)


@dp.callback_query(F.data == 'add_korzinka_product32')
async def add_kor(call: types.CallbackQuery):
    print(type(product16.price))
    print(type(product16.title))
    print(type(product16.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kenlin Koylak", product16.price, product16.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys32')
async def add_kor(call: types.CallbackQuery):
    print(type(product16.price))
    print(type(product16.title))
    print(type(product16.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kenlin Koylak", product16.price, product16.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Zegra Oiasi🧢")
async def send_product_info(message: types.Message):
    messages, photos = product17.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kepka_oiasi)


@dp.callback_query(F.data == 'add_korzinka_product33')
async def add_kor(call: types.CallbackQuery):
    print(type(product17.price))
    print(type(product17.title))
    print(type(product17.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Zegra Oiasi🧢", product17.price, product17.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys33')
async def add_kor(call: types.CallbackQuery):
    print(type(product17.price))
    print(type(product17.title))
    print(type(product17.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Zegra Oiasi🧢", product17.price, product17.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Zegna wollen🧢")
async def send_product_info(message: types.Message):
    messages, photos = product18.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kepka_wollen)


@dp.callback_query(F.data == 'add_korzinka_product34')
async def add_kor(call: types.CallbackQuery):
    print(type(product18.price))
    print(type(product18.title))
    print(type(product18.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Zegna wollen🧢", product18.price, product18.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys34')
async def add_kor(call: types.CallbackQuery):
    print(type(product18.price))
    print(type(product18.title))
    print(type(product18.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Zegna wollen🧢", product18.price, product18.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Polo Ralph🧢")
async def send_product_info(message: types.Message):
    messages, photos = product19.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kepka_ralph)


@dp.callback_query(F.data == 'add_korzinka_product35')
async def add_kor(call: types.CallbackQuery):
    print(type(product19.price))
    print(type(product19.title))
    print(type(product19.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Polo Ralph🧢", product19.price, product19.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys35')
async def add_kor(call: types.CallbackQuery):
    print(type(product19.price))
    print(type(product19.title))
    print(type(product19.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Polo Ralph🧢", product19.price, product19.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Tommy Hifiger🧢")
async def send_product_info(message: types.Message):
    messages, photos = product20.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kepka_hifiger)


@dp.callback_query(F.data == 'add_korzinka_product36')
async def add_kor(call: types.CallbackQuery):
    print(type(product20.price))
    print(type(product20.title))
    print(type(product20.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Tommy Hifiger🧢", product20.price, product20.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys36')
async def add_kor(call: types.CallbackQuery):
    print(type(product20.price))
    print(type(product20.title))
    print(type(product20.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Tommy Hifiger🧢", product20.price, product20.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Romol🧣')
async def cmd_product(message: types.Message):
    await message.answer("Romol rangini Tanlang!"
                         "", reply_markup=romoll)


@dp.message(F.text == "Kulirang🩶")
async def send_product_info(message: types.Message):
    messages, photos = product21.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=romol_kuli)


@dp.callback_query(F.data == 'add_korzinka_product37')
async def add_kor(call: types.CallbackQuery):
    print(type(product21.price))
    print(type(product21.title))
    print(type(product21.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kulirang🩶", product21.price, product21.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys37')
async def add_kor(call: types.CallbackQuery):
    print(type(product21.price))
    print(type(product21.title))
    print(type(product21.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kulirang🩶", product21.price, product21.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Romol_Oq⚪")
async def send_product_info(message: types.Message):
    messages, photos = product22.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=romol_oq)


@dp.callback_query(F.data == 'add_korzinka_product38')
async def add_kor(call: types.CallbackQuery):
    print(type(product22.price))
    print(type(product22.title))
    print(type(product22.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Romol_Oq⚪", product22.price, product22.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys38')
async def add_kor(call: types.CallbackQuery):
    print(type(product22.price))
    print(type(product22.title))
    print(type(product22.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Romol_Oq⚪", product22.price, product22.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Romol_Qora⚫")
async def send_product_info(message: types.Message):
    messages, photos = product23.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=romol_qora)


@dp.callback_query(F.data == 'add_korzinka_product39')
async def add_kor(call: types.CallbackQuery):
    print(type(product23.price))
    print(type(product23.title))
    print(type(product23.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Romol_Qora⚫", product23.price, product23.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys39')
async def add_kor(call: types.CallbackQuery):
    print(type(product23.price))
    print(type(product23.title))
    print(type(product23.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Romol_Qora⚫", product23.price, product23.quantity))
    db_connect.commit()
    await call.answer("Product added!")


# @dp.message(F.text == "Finka")
# async def send_product_info(message: types.Message):
#     messages, photos = product8.send_product_info()
#     print(photos)
#     await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=koylak)
#

@dp.message(F.text == 'Sumka💼')
async def cmd_product(message: types.Message):
    await message.answer("Sumka Turini kirgazing!"
                         "", reply_markup=sumka)


@dp.message(F.text == "Prada")
async def send_product_info(message: types.Message):
    messages, photos = product24.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=prada_s)


@dp.callback_query(F.data == 'add_korzinka_product40')
async def add_kor(call: types.CallbackQuery):
    print(type(product24.price))
    print(type(product24.title))
    print(type(product24.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Prada", product24.price, product24.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys40')
async def add_kor(call: types.CallbackQuery):
    print(type(product24.price))
    print(type(product24.title))
    print(type(product24.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Prada", product24.price, product24.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Monnalisa")
async def send_product_info(message: types.Message):
    messages, photos = product25.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=monna_s)


@dp.callback_query(F.data == 'add_korzinka_product41')
async def add_kor(call: types.CallbackQuery):
    print(type(product25.price))
    print(type(product25.title))
    print(type(product25.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Monnalisa", product25.price, product25.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys41')
async def add_kor(call: types.CallbackQuery):
    print(type(product25.price))
    print(type(product25.title))
    print(type(product25.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Prada", product25.price, product25.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Saint Laurent")
async def send_product_info(message: types.Message):
    messages, photos = product26.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=sait_s)


@dp.callback_query(F.data == 'add_korzinka_product42')
async def add_kor(call: types.CallbackQuery):
    print(type(product26.price))
    print(type(product26.title))
    print(type(product26.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Saint Laurent", product26.price, product26.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys42')
async def add_kor(call: types.CallbackQuery):
    print(type(product26.price))
    print(type(product26.title))
    print(type(product26.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Saint Laurent", product26.price, product26.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Alexender")
async def send_product_info(message: types.Message):
    messages, photos = product27.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=alexan_s)


@dp.callback_query(F.data == 'add_korzinka_product43')
async def add_kor(call: types.CallbackQuery):
    print(type(product27.price))
    print(type(product27.title))
    print(type(product27.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Alexender", product27.price, product27.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys43')
async def add_kor(call: types.CallbackQuery):
    print(type(product27.price))
    print(type(product27.title))
    print(type(product27.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Alexender", product27.price, product27.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Qishki Kiyimlar⛄')
async def cmd_product(message: types.Message):
    await message.answer("Sumka Turini kirgazing!"
                         "", reply_markup=qiwki_kiym)


@dp.message(F.text == "Kurtka🧥")
async def send_product_info(message: types.Message):
    messages, photos = product28.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kurtka)


@dp.callback_query(F.data == 'add_korzinka_product44')
async def add_kor(call: types.CallbackQuery):
    print(type(product28.price))
    print(type(product28.title))
    print(type(product28.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Kurtka🧥", product28.price, product28.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys44')
async def add_kor(call: types.CallbackQuery):
    print(type(product28.price))
    print(type(product28.title))
    print(type(product28.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kurtka🧥", product28.price, product28.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Palto🧥")
async def send_product_info(message: types.Message):
    messages, photos = product29.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=palto)


@dp.callback_query(F.data == 'add_korzinka_product45')
async def add_kor(call: types.CallbackQuery):
    print(type(product29.price))
    print(type(product29.title))
    print(type(product29.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Palto🧥", product29.price, product29.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys45')
async def add_kor(call: types.CallbackQuery):
    print(type(product29.price))
    print(type(product29.title))
    print(type(product29.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Palto🧥", product29.price, product29.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Jemper")
async def send_product_info(message: types.Message):
    messages, photos = product30.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=jemper)


@dp.callback_query(F.data == 'add_korzinka_product46')
async def add_kor(call: types.CallbackQuery):
    print(type(product30.price))
    print(type(product30.title))
    print(type(product30.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Jemper", product30.price, product30.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys46')
async def add_kor(call: types.CallbackQuery):
    print(type(product30.price))
    print(type(product30.title))
    print(type(product30.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Jemper", product30.price, product30.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Kuzgi Koylak')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim Turini kirgazing!"
                         "", reply_markup=kuzgi_kiym_bola)


@dp.message(F.text == "Burbery_bola")
async def send_product_info(message: types.Message):
    messages, photos = product63.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=burbery)


@dp.callback_query(F.data == 'add_korzinka_product92')
async def add_kor(call: types.CallbackQuery):
    print(type(product63.price))
    print(type(product63.title))
    print(type(product63.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Burbery_bola", product63.price, product63.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys92')
async def add_kor(call: types.CallbackQuery):
    print(type(product63.price))
    print(type(product63.title))
    print(type(product63.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Burbery_bola", product63.price, product63.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Tullen_bola")
async def send_product_info(message: types.Message):
    messages, photos = product64.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=tullen)


@dp.callback_query(F.data == 'add_korzinka_product93')
async def add_kor(call: types.CallbackQuery):
    print(type(product64.price))
    print(type(product64.title))
    print(type(product64.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Tullen_bola", product64.price, product64.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys93')
async def add_kor(call: types.CallbackQuery):
    print(type(product64.price))
    print(type(product64.title))
    print(type(product64.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Tullen_bola", product64.price, product64.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Sandro_bola")
async def send_product_info(message: types.Message):
    messages, photos = product65.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=sandro)


@dp.callback_query(F.data == 'add_korzinka_product94')
async def add_kor(call: types.CallbackQuery):
    print(type(product65.price))
    print(type(product65.title))
    print(type(product65.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Sandro_bola", product65.price, product65.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys94')
async def add_kor(call: types.CallbackQuery):
    print(type(product65.price))
    print(type(product65.title))
    print(type(product65.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Sandro_bola", product65.price, product65.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Qishki Koylak')
async def cmd_product(message: types.Message):
    await message.answer("Kiyim Turini kirgazing!"
                         "", reply_markup=qiwki_kiym_bola)


@dp.message(F.text == "Kurtka🧥_bola")
async def send_product_info(message: types.Message):
    messages, photos = product60.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=kurtka_bola)


@dp.callback_query(F.data == 'add_korzinka_product89')
async def add_kor(call: types.CallbackQuery):
    print(type(product60.price))
    print(type(product60.title))
    print(type(product60.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Kurtka🧥_bola", product60.price, product60.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys89')
async def add_kor(call: types.CallbackQuery):
    print(type(product60.price))
    print(type(product60.title))
    print(type(product60.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Kurtka🧥_bola", product60.price, product60.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Palto🧥_bola")
async def send_product_info(message: types.Message):
    messages, photos = product61.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=palto_bola)


@dp.callback_query(F.data == 'add_korzinka_product90')
async def add_kor(call: types.CallbackQuery):
    print(type(product61.price))
    print(type(product61.title))
    print(type(product61.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Palto🧥_bola", product61.price, product61.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys90')
async def add_kor(call: types.CallbackQuery):
    print(type(product61.price))
    print(type(product61.title))
    print(type(product61.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Palto🧥_bola", product61.price, product61.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Jemper_bola")
async def send_product_info(message: types.Message):
    messages, photos = product62.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=jumper_bola)


@dp.callback_query(F.data == 'add_korzinka_product91')
async def add_kor(call: types.CallbackQuery):
    print(type(product62.price))
    print(type(product62.title))
    print(type(product62.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Jemper_bola", product62.price, product62.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys91')
async def add_kor(call: types.CallbackQuery):
    print(type(product62.price))
    print(type(product62.title))
    print(type(product62.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Jemper_bola", product62.price, product62.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == 'Shim👖')
async def cmd_product(message: types.Message):
    await message.answer("Shim"
                         " Turini kirgazing!"
                         "", reply_markup=erke_wim)


@dp.message(F.text == "Brunello👖")
async def send_product_info(message: types.Message):
    messages, photos = product31.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=wm_bronell)


@dp.callback_query(F.data == 'add_korzinka_product47')
async def add_kor(call: types.CallbackQuery):
    print(type(product31.price))
    print(type(product31.title))
    print(type(product31.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Brunello👖", Product1.price, Product1.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys47')
async def add_kor(call: types.CallbackQuery):
    print(type(product31.price))
    print(type(product31.title))
    print(type(product31.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Brunello👖", product31.price, product31.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Zegna👖")
async def send_product_info(message: types.Message):
    messages, photos = product32.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=wm_zegna)


@dp.callback_query(F.data == 'add_korzinka_product48')
async def add_kor(call: types.CallbackQuery):
    print(type(product32.price))
    print(type(product32.title))
    print(type(product32.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Zegna👖", product32.price, product32.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys48')
async def add_kor(call: types.CallbackQuery):
    print(type(product32.price))
    print(type(product32.title))
    print(type(product32.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Zegna👖", product32.price, product32.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Polo Ralph👖")
async def send_product_info(message: types.Message):
    messages, photos = product33.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=wm_polo)


@dp.callback_query(F.data == 'add_korzinka_product49')
async def add_kor(call: types.CallbackQuery):
    print(type(product33.price))
    print(type(product33.title))
    print(type(product33.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Polo Ralph👖", product33.price, product33.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys49')
async def add_kor(call: types.CallbackQuery):
    print(type(product33.price))
    print(type(product33.title))
    print(type(product33.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Polo Ralph👖", product33.price, product33.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.message(F.text == "Sartoria👖")
async def send_product_info(message: types.Message):
    messages, photos = product34.send_product_info()
    print(photos)
    await message.answer_photo(photo=FSInputFile(photos), caption=messages, reply_markup=wm_satori)


@dp.callback_query(F.data == 'add_korzinka_product50')
async def add_kor(call: types.CallbackQuery):
    print(type(product34.price))
    print(type(product34.title))
    print(type(product34.quantity))
    db_cursor.execute("""
        INSERT INTO Korzina (title, price, quantity)
        VALUES (?, ?, ?)    
        """, ("Sartoria👖", product34.price, product34.quantity))
    db_connect.commit()
    await call.answer("Product added!")


@dp.callback_query(F.data == 'add_buys50')
async def add_kor(call: types.CallbackQuery):
    print(type(product34.price))
    print(type(product34.title))
    print(type(product34.quantity))
    db_cursor.execute("""
        INSERT INTO Buys (title, price, quantity)
        VALUES (?, ?, ?)
        """, ("Sartoria👖", product34.price, product34.quantity))
    db_connect.commit()
    await call.answer("Product added!")


async def main():
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
