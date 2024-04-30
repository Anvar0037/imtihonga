from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Mahsulotlarni ko'rish", callback_data='get_all_product')],
    [InlineKeyboardButton(text="Mahsulot qo'shish", callback_data='add_product')]
])

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Kiyimlar🥻'),
     KeyboardButton(text='Aksessuar'),
     KeyboardButton(text='Korzina'),
     KeyboardButton(text='Sotib Olganlarim')]
], resize_keyboard=True)

buy_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🛒', callback_data='savatchaga'),
         InlineKeyboardButton(text='💸', callback_data='sotib olganlarim')]

    ])

erke_koylela = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Spartivka"),
     KeyboardButton(text="Futbolka")],
    [KeyboardButton(text="Shortik"),
     KeyboardButton(text="⬅️ Ortga")]
], resize_keyboard=True)

spotivka = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Boss Kidswear'),
     KeyboardButton(text='Billionarie')],
    [KeyboardButton(text='⬅️ Ortga')]
])

futbolka_erke = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Prada'),
     KeyboardButton(text='Calvin')],
    [KeyboardButton(text='Boss'),
     KeyboardButton(text='⬅️ Ortga')]
])
caqalo = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Body'),
     KeyboardButton(text='Kombenizon')],
    [KeyboardButton(text='Qishki Koylak'),
     KeyboardButton(text='Kuzgi Koylak'),
     KeyboardButton(text='⬅️ Ortga')]
])

shortika = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Moschino'),
     KeyboardButton(text='Trussardi')],
    [KeyboardButton(text='⬅️ Ortga')]
])

Ogil_bollar_kiymi = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Shim👖'),
     KeyboardButton(text='Koylaklar👕')],
    [KeyboardButton(text='Krasofka'),
     KeyboardButton(text='Kepkalar🎓')],
    [KeyboardButton(text='Popka💼'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)
erke_kepka = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Oltin Gerbi'),
     KeyboardButton(text='Kepka-Art')],
    [KeyboardButton(text='Golovnie ubori'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

erke_popka = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Oq Popka"),
     KeyboardButton(text="Qora Popka")],
    [KeyboardButton(text="️⬅️ Ortga")]
], resize_keyboard=True)

aksesuar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Achki🕶️'),
     KeyboardButton(text='Rimen')],
    [KeyboardButton(text='Mayka'),
     KeyboardButton(text='Naski🧦'),
     KeyboardButton(text=''),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

kym_turi = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Ayollar kiyimi👧'),
     KeyboardButton(text='Erkaklar Kiyimi👨'),
     KeyboardButton(text='Chaqaloqlar Kiyimi👶')]
], resize_keyboard=True)
body = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Oq'),
     KeyboardButton(text='Qora')],
    [KeyboardButton(text='Sariq'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

qizlar_kiymi = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Yupka'),
     KeyboardButton(text='Koylak👕')],
    [KeyboardButton(text='Tuflik👢'),
     KeyboardButton(text='Kepka🎓')],
    [KeyboardButton(text='Sumka💼'),
     KeyboardButton(text='Romol🧣'),
     KeyboardButton(text=''),
     KeyboardButton(text='Qishki Kiyimlar⛄'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

Tuflik = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Loro Piana👟'),
     KeyboardButton(text='Adidas👟')],
    [KeyboardButton(text='Nike👟'),
     KeyboardButton(text='Gucci👟'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

krasofka = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Loro Piana-k👟'),
     KeyboardButton(text='Adidas-k👟')],
    [KeyboardButton(text='Nike-k👟'),
     KeyboardButton(text='Gucci-k👟'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

qiwki_kiym = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kurtka🧥"),
     KeyboardButton(text="Palto🧥")],
    [KeyboardButton(text="Jemper"),
     KeyboardButton(text="⬅️ Ortga")]
], resize_keyboard=True)


qiwki_kiym_bola = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kurtka🧥_bola"),
     KeyboardButton(text="Palto🧥_bola")],
    [KeyboardButton(text="Jemper_bola"),
     KeyboardButton(text="⬅️ Ortga")]
], resize_keyboard=True)


kuzgi_kiym_bola = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Burbery_bola"),
     KeyboardButton(text="Tullen_bola")],
    [KeyboardButton(text="Sandro_bola"),
     KeyboardButton(text="⬅️ Ortga")]
], resize_keyboard=True)

kombeniz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Sariq"),
     KeyboardButton(text="Kok")],
    [KeyboardButton(text="Qora"),
     KeyboardButton(text="⬅️ Ortga")]
], resize_keyboard=True)

# yupka
yupka_razmer = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='XXS--38'),
     KeyboardButton(text='XS--40')],
    [KeyboardButton(text='S--42'),
     KeyboardButton(text='M--44')],
    [KeyboardButton(text='L--46'),
     KeyboardButton(text='XL--48')],
    [KeyboardButton(text='XXL--49'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

yupka_rangXXS = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora⚫'),
     KeyboardButton(text='Kok🔵')],
    [KeyboardButton(text='Pushti🩷'),
     KeyboardButton(text='Yashil🟢'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

yupka_rangXS = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora⚫'),
     KeyboardButton(text='Kok🔵')],
    [KeyboardButton(text='Pushti🩷'),
     KeyboardButton(text='Yashil🟢'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

yupka_rangX42 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora⚫'),
     KeyboardButton(text='Kok🔵')],
    [KeyboardButton(text='Pushti🩷'),
     KeyboardButton(text='Yashil🟢'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

yupka_rangM44 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora⚫'),
     KeyboardButton(text='Kok🔵')],
    [KeyboardButton(text='Pushti🩷'),
     KeyboardButton(text='Yashil🟢'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

yupka_rangL46 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora⚫'),
     KeyboardButton(text='Kok🔵')],
    [KeyboardButton(text='Pushti🩷'),
     KeyboardButton(text='Yashil🟢'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

yupka_rangXL48 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora⚫'),
     KeyboardButton(text='Kok🔵')],
    [KeyboardButton(text='Pushti🩷'),
     KeyboardButton(text='Yashil🟢'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)
yupka_rangXXL49 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora⚫'),
     KeyboardButton(text='Kok🔵')],
    [KeyboardButton(text='Pushti🩷'),
     KeyboardButton(text='Yashil🟢'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

tuflik = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product1'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys1')]
])

koylak = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Futbolka👕'),
     KeyboardButton(text='Finka')],
    [KeyboardButton(text='Oq Koylak⚪'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

furbolka = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora rangli⚫'),
     KeyboardButton(text='Kok rangli🔵')],
    [KeyboardButton(text='Oq rangli⚪'),
     KeyboardButton(text='Pushti rangli🩷'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

tufli_razmer_loro = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Loro-36'),
     KeyboardButton(text='Loro-37')],
    [KeyboardButton(text='Loro-38'),
     KeyboardButton(text='Loro-39')],
    [KeyboardButton(text='Loro-40'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

krasof_razmer_loro = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Krasofka-39')],
    [KeyboardButton(text='Krasofka-40'),
     KeyboardButton(text='')],
    [KeyboardButton(text='Krasofka-41'),
     KeyboardButton(text="Krasofka-42"),
     KeyboardButton(text="️⬅️ Ortga")]
], resize_keyboard=True)

krasof_razmer_adi = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Adidas-Krasofka-39')],
    [KeyboardButton(text='Adidas-Krasofka-40'),
     KeyboardButton(text='')],
    [KeyboardButton(text='Adidas-Krasofka-41'),
     KeyboardButton(text="Adidas-Krasofka-42"),
     KeyboardButton(text="️⬅️ Ortga")]
], resize_keyboard=True)

krasof_razmer_nike = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Nike-Krasofka-39')],
    [KeyboardButton(text='Nike-Krasofka-40'),
     KeyboardButton(text='')],
    [KeyboardButton(text='Nike-Krasofka-41'),
     KeyboardButton(text="Nike-Krasofka-42"),
     KeyboardButton(text="️⬅️ Ortga")]
], resize_keyboard=True)

krasof_razmer_gucci = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Gucci-Krasofka-39')],
    [KeyboardButton(text='Gucci-Krasofka-40'),
     KeyboardButton(text='')],
    [KeyboardButton(text='Gucci-Krasofka-41'),
     KeyboardButton(text="Gucci-Krasofka-42"),
     KeyboardButton(text="️⬅️ Ortga")]
], resize_keyboard=True)

tufli_razmer_adidas = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Adidas-36'),
     KeyboardButton(text='Adidas-37')],
    [KeyboardButton(text='Adidas-38'),
     KeyboardButton(text='Adidas-39')],
    [KeyboardButton(text='Adidas-40'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

tufli_razmer_nike = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Nike-36'),
     KeyboardButton(text='Nike-37')],
    [KeyboardButton(text='Nike-38'),
     KeyboardButton(text='Nike-39')],
    [KeyboardButton(text='Nike-40'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

tufli_razmer_gucci = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Gucci-36'),
     KeyboardButton(text='Gucci-37')],
    [KeyboardButton(text='Gucci-38'),
     KeyboardButton(text='Gucci-39')],
    [KeyboardButton(text='Gucci-40'),
     KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

finkaa = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora Rangli⚫'),
     KeyboardButton(text='Kok Rangli🔵')],
    [KeyboardButton(text='Oq Rangli⚪'),
     KeyboardButton(text='️⬅️ Ortga')],
], resize_keyboard=True)


finkaa = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Qora Rangli⚫'),
     KeyboardButton(text='Kok Rangli🔵')],
    [KeyboardButton(text='Oq Rangli⚪'),
     KeyboardButton(text='️⬅️ Ortga')],
], resize_keyboard=True)

oq_koyle = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Kenlin Koylak'),
     KeyboardButton(text='️⬅️ Ortga')],
], resize_keyboard=True)

kepkaa = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Zegra Oiasi🧢"),
     KeyboardButton(text="Zegna wollen🧢")],
    [KeyboardButton(text="Polo Ralph🧢"),
     KeyboardButton(text="Tommy Hifiger🧢"),
     KeyboardButton(text="️⬅️ Ortga")],
], resize_keyboard=True)

romoll = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kulirang🩶"),
     KeyboardButton(text="Romol_Oq⚪")],
    [KeyboardButton(text="Romol_Qora⚫"),
     KeyboardButton(text="️⬅️ Ortga")]
], resize_keyboard=True)

sumka = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Prada"),
     KeyboardButton(text="Monnalisa")],
    [KeyboardButton(text="Saint Laurent"),
     KeyboardButton(text="Alexender"),
     KeyboardButton(text="️⬅️ Ortga")]
], resize_keyboard=True)

erke_wim = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Brunello👖"),
     KeyboardButton(text="Zegna👖")],
    [KeyboardButton(text="Polo Ralph👖"),
     KeyboardButton(text="Sartoria👖"),
     KeyboardButton(text="️⬅️ Ortga")]
], resize_keyboard=True)

loro_37 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product2'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys2')]
])

loro_38 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product3'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys3')]
])

loro_39 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product4'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys4')]
])
loro_40 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product5'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys5')]
])

adidas36 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product6'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys6')]
])

adidas37 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product7'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys7')]
])
adidas38 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product8'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys8')]
])
adidas39 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product9'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys9')]
])
adidas40 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product10'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys10')]
])
nike_36 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product11'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys11')]
])
nike_37 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product12'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys12')]
])
nike_38 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product13'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys13')]
])
nike_39 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product14'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys14')]
])
nike_40 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product15'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys15')]
])
gucci_36 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product16'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys16')]
])
gucci_37 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product17'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys17')]
])
gucci_38 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product18'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys18')]
])
gucci_39 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product19'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys19')]
])
gucci_40 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product20'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys20')]
])
yupka_qora = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product21'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys21')]
])
yupka_kok = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product22'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys22')]
])
yupka_pushti = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product23'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys23')]
])

yupka_yashil = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product24'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys24')]
])

qora_fotbol = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product25'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys25')]
])

kok_futbol = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product26'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys26')]
])

oq_futbol = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product27'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys27')]
])

puwti_futbol = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product28'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys28')]
])

qora_finka = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product29'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys29')]
])
oq_finka = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product30'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys30')]
])
kok_finka = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product31'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys31')]
])
keln_koyle = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product32'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys32')]
])
kepka_oiasi = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product33'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys33')]
])
kepka_wollen = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product34'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys34')]
])
kepka_ralph = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product35'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys35')]
])
kepka_hifiger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product36'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys36')]
])
romol_kuli = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product37'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys37')]
])
romol_oq = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product38'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys38')]
])
romol_qora = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product39'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys39')]
])
prada_s = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product40'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys40')]
])
monna_s = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product41'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys41')]
])
sait_s = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product42'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys42')]
])
alexan_s = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product43'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys43')]
])
kurtka = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product44'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys44')]
])
palto = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product45'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys45')]
])
jemper = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product46'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys46')]
])
wm_bronell = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product47'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys47')]
])
wm_zegna = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product48'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buy48')]
])
wm_polo = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product49'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys49')]
])
wm_satori = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product50'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys50')]
])
loro_kras = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product51'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys51')]
])
loro_kras40 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product52'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys52')]
])
loro_kras41 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product53'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys53')]
])
loro_kras42 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product54'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys54')]
])
adi_kras39 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product55'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys55')]
])
adi_kras40 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product56'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys56')]
])
adi_kras41 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product57'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys57')]
])
adi_kras42 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product58'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys58')]
])
nike_kras39 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product59'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys59')]
])
nike_kras40 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product60'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys60')]
])
nike_kras41 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product61'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys61')]
])
nike_kras42 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product62'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys62')]
])
gucci_kras39 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product63'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys63')]
])
gucci_kras40 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product64'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys64')]
])
gucci_kras41 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product65'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys65')]
])
gucci_kras42 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product66'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys66')]
])
oq_popka = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product67'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys67')]
])
qora_popka = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product68'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys68')]
])
boss_kids = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product69'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys69')]
])
bilio = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product70'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys70')]
])
fut_prada = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product71'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys71')]
])
fut_calvin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product72'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys72')]
])
fut_boss = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product73'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys73')]
])
moscino = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product74'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys74')]
])
trussardi = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product75'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys75')]
])
oltn_gerb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product76'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys76')]
])
kepka_art = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product77'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys77')]
])
golovni_u = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product78'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys78')]
])
bodyy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product79'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys79')]
])
kombezon = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product80'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys80')]
])
kuzgi = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product81'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys81')]
])
qiwki_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product82'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys82')]
])
oq_body = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product83'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys83')]
])
sarq_b = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product84'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys84')]
])
qora_b = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product85'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys85')]
])
sarq_kombeniz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product86'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys86')]
])
kok_kombeniz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product87'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys87')]
])
qora_kombeniz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product88'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys88')]
])


kurtka_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product89'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys89')]
])


palto_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product90'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys90')]
])


jumper_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product91'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys91')]
])
burbery = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product92'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys92')]
])


tullen = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product93'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys93')]
])
sandro = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product94'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys94')]
])


jumper_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product95'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys95')]
])
palto_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product96'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys96')]
])


jumper_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product97'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys97')]
])
palto_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product98'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys98')]
])


jumper_bola = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Korzina', callback_data='add_korzinka_product91'),
     InlineKeyboardButton(text='+', callback_data='add_remove1')],
    [InlineKeyboardButton(text='Sotib Olganlarim', callback_data='add_buys11')]
])
