class Product:
    def __init__(self, title, price, description, photo, quantity):
        self.title = title
        self.price = price
        self.description = description
        self.photo = photo
        self.quantity = quantity

    def send_product_info(self):
        return f"{self.title}\n\n{self.description}\n\n{self.price}00 сум\n\nКоличество - {self.quantity}", self.photo


Product1 = Product("Loro Piana👟", 500,
                   "Loro Piana — итальянская компания. Производитель одежды из шерсти и кашемира класса люкс.\n"
                   " Штаб-квартира компании расположена в итальянском городе Куарона. Со дня своего основания являлась\n"
                   " крупнейшим производителем премиальных изделий из кашемира и сверхтонкой шерсти. В декабре 2013 года 80 % \n"
                   "компании купил французский люксовый холдинг LVMH. Компания располагает 2 собственными фабриками.",
                   "img.png", 1)

Product2 = Product("Adidas", 450.000,
                   "adidas is about more than sportswear and workout clothes. We partner with the best in the industry to co-create."
                   " This way we offer our fans the sporting goods, style and clothing that match the athletic needs, while keeping \n"
                   "sustainability in mind. We’re here to support creators. Improve their game. Create change. And we think about the \n"
                   "impact we have on our world",
                   "img_1.png", 1)

product3 = Product("Nike👟", 450.000,
                   "Nike, Inc.[note 1] (stylized as NIKE) is an American athletic footwear and apparel\n"
                   " corporation headquartered near Beaverton, Oregon, United States.[5] It is the world's \n"
                   "largest supplier of athletic shoes and apparel and a major manufacturer of sports equipment,\n"
                   " with revenue in excess of US$46 billion in its fiscal year 2022.[6][7]",
                   "img_2.png", 1)

product4 = Product("Gucci👟", 450.000,
                   "Guccio Gucci S.p.A.,[1][2] doing business as Gucci (/ˈɡuːtʃi/ ⓘ GOO-chee, Italian:\n"
                   " [ˈɡuttʃi]), is an Italian luxury fashion house based in Florence, Italy.[3][4][5] Its product\n"
                   " lines include handbags, ready-to-wear, footwear, accessories, and home decoration;\n"
                   " and it licenses its name and branding to Coty for fragrance and cosmetics under the name Gucci Beauty.[6]",
                   "img_3.png", 1)

product5 = Product("Qora⚫", 700.000,
                   "7-10 yoshli qizlar uchun qora burmali yubka har qanday vaziyatga mos keladigan klassik\n"
                   " elementidir. U kiyish paytida chidamlilik va qulaylikni ta'minlaydigan yuqori sifatli\n"
                   " materialdan tayyorlangan. Yubka o'rta uzunlikda va burmalar bilan bezatilgan bo'lib,\n"
                   " unga nafislik qo'shadi. Kiyinish qulay bo'lishi uchun kamarш elastik tasmadan tikilgan.\n"
                   " Ushbu model bluzkalar bilan juda mos keladi, maktab yoki \n"
                   "bayram tadbirlari uchun zamonaviy va qulay ko'rinish yaratadi.",
                   "img_4.png", 1)

product6 = Product("Kok🔵", 400.000,
                   "7-10 yoshli qizlar uchun kok burmali yubka har qanday vaziyatga mos keladigan klassik\n"
                   " elementidir. U kiyish paytida chidamlilik va qulaylikni ta'minlaydigan yuqori sifatli\n"
                   " materialdan tayyorlangan. Yubka o'rta uzunlikda va burmalar bilan bezatilgan bo'lib,\n"
                   " unga nafislik qo'shadi. Kiyinish qulay bo'lishi uchun kamarш elastik tasmadan tikilgan.\n"
                   " Ushbu model bluzkalar bilan juda mos keladi, maktab yoki \n"
                   "bayram tadbirlari uchun zamonaviy va qulay ko'rinish yaratadi.",
                   "img_5.png", 1)

product7 = Product("Pushti🩷", 500.000,
                   "7-10 yoshli qizlar uchun pushti burmali yubka har qanday vaziyatga mos keladigan klassik\n"
                   " elementidir. U kiyish paytida chidamlilik va qulaylikni ta'minlaydigan yuqori sifatli\n"
                   " materialdan tayyorlangan. Yubka o'rta uzunlikda va burmalar bilan bezatilgan bo'lib,\n"
                   " unga nafislik qo'shadi. Kiyinish qulay bo'lishi uchun kamarш elastik tasmadan tikilgan.\n"
                   " Ushbu model bluzkalar bilan juda mos keladi, maktab yoki \n"
                   "bayram tadbirlari uchun zamonaviy va qulay ko'rinish yaratadi.",
                   "img_6.png", 1)

product8 = Product("Yashil🟢", 600.000,
                   "7-10 yoshli qizlar uchun yashil burmali yubka har qanday vaziyatga mos keladigan klassik\n"
                   " elementidir. U kiyish paytida chidamlilik va qulaylikni ta'minlaydigan yuqori sifatli\n"
                   " materialdan tayyorlangan. Yubka o'rta uzunlikda va burmalar bilan bezatilgan bo'lib,\n"
                   " unga nafislik qo'shadi. Kiyinish qulay bo'lishi uchun kamarш elastik tasmadan tikilgan.\n"
                   " Ushbu model bluzkalar bilan juda mos keladi, maktab yoki \n"
                   "bayram tadbirlari uchun zamonaviy va qulay ko'rinish yaratadi.",
                   "img_7.png", 1)

product9 = Product("Qora rangli⚫", 150.000,
                   "Футболки делятся на два типа в зависимости от того, к какой категории белья они относятся\n"
                   " — нижние (надеваются под другую одежду в качестве нательного слоя) и верхние \n"
                   "(могут выставляться напоказ, то есть не покрываться никакой одеждой). Первые также называются \n"
                   "нижними сорочками, они могут надеваться под рубашку (верхнюю сорочку), либо под плечевую одежду \n"
                   "(свитера, джемперы, пуловеры, толстовки, кофты). От них произошли современные верхние футболки,\n"
                   " носящиеся непокрытыми другой одеждой, либо в сочетании с чем-то.\n"
                   " На таких футболках могут размещаться надписи, узоры, изображения.",
                   "img_8.png", 1)

product10 = Product("Kok rangli🔵", 100.000,
                    "Футболки делятся на два типа в зависимости от того, к какой категории белья они относятся\n"
                    " — нижние (надеваются под другую одежду в качестве нательного слоя) и верхние \n"
                    "(могут выставляться напоказ, то есть не покрываться никакой одеждой). Первые также называются \n"
                    "нижними сорочками, они могут надеваться под рубашку (верхнюю сорочку), либо под плечевую одежду \n"
                    "(свитера, джемперы, пуловеры, толстовки, кофты). От них произошли современные верхние футболки,\n"
                    " носящиеся непокрытыми другой одеждой, либо в сочетании с чем-то.\n"
                    " На таких футболках могут размещаться надписи, узоры, изображения.",
                    "img_10.png", 1)

product11 = Product("Oq rangli⚪", 90.000,
                    "Футболки делятся на два типа в зависимости от того, к какой категории белья они относятся\n"
                    " — нижние (надеваются под другую одежду в качестве нательного слоя) и верхние \n"
                    "(могут выставляться напоказ, то есть не покрываться никакой одеждой). Первые также называются \n"
                    "нижними сорочками, они могут надеваться под рубашку (верхнюю сорочку), либо под плечевую одежду \n"
                    "(свитера, джемперы, пуловеры, толстовки, кофты). От них произошли современные верхние футболки,\n"
                    " носящиеся непокрытыми другой одеждой, либо в сочетании с чем-то.\n"
                    " На таких футболках могут размещаться надписи, узоры, изображения.",
                    "img_9.png", 1)

product12 = Product("Pushti rangli🩷", 110.000,
                    "Футболки делятся на два типа в зависимости от того, к какой категории белья они относятся\n"
                    " — нижние (надеваются под другую одежду в качестве нательного слоя) и верхние \n"
                    "(могут выставляться напоказ, то есть не покрываться никакой одеждой). Первые также называются \n"
                    "нижними сорочками, они могут надеваться под рубашку (верхнюю сорочку), либо под плечевую одежду \n"
                    "(свитера, джемперы, пуловеры, толстовки, кофты). От них произошли современные верхние футболки,\n"
                    " носящиеся непокрытыми другой одеждой, либо в сочетании с чем-то.\n"
                    " На таких футболках могут размещаться надписи, узоры, изображения.",
                    "img_11.png", 1)

product13 = Product("Qora Rangli⚫", 110.000,
                    "Ayollar finka-futbolkasi Poli, oq, qora va qizil. 4.8 (32 sharhlar). \n"
                    "9 000 so'm/oyiga. 149 000 so'm 75 000 so'm. Ayollar futbolka-polosi. Aksiya. Ayollar",
                    "img_13.png", 1)

product14 = Product("Kok Rangli🔵", 110.000,
                    "Ayollar finka-futbolkasi Poli, oq, qora va qizil. 4.8 (32 sharhlar). \n"
                    "9 000 so'm/oyiga. 149 000 so'm 75 000 so'm. Ayollar futbolka-polosi. Aksiya. Ayollar",
                    "img_15.png", 1)

product15 = Product("Oq Rangli⚪", 110.000,
                    "Ayollar finka-futbolkasi Poli, oq, qora va qizil. 4.8 (32 sharhlar). \n"
                    "9 000 so'm/oyiga. 149 000 so'm 75 000 so'm. Ayollar futbolka-polosi. Aksiya. Ayollar",
                    "img_14.png", 1)

product16 = Product("Oq Koylak⚪", 600.000,
                    'Oʻzbek ayollarining milliy liboslari — oʻzbek xalqining tarixdagi kiyim-kechaklari \n'
                    'bilan bogʻliq maʼlumotlarni arxeologik qazilmalar jarayonida topilgan qadimiy',
                    "img_17.png", 1)

product17 = Product("Zegra Oiasi🧢", 100.000,
                    "Kepining beysbol kepkasi futbol o'ynash, yugurish,,\n"
                    " velosipedda yurish va boshqa sport turlari uchun ham mos keladi.",
                    "img_18.png", 1)

product18 = Product("Zegna wollen🧢", 70.000,
                    "Kepining beysbol kepkasi   c futbol o'ynash, yugurish,,\n"
                    " velosipedda yurish va boshqa sport turlari uchun ham mos keladi",
                    "img_19.png", 1)

product19 = Product("Polo Ralph🧢", 120.000,
                    "Kepining beysbol kepkasi futbol o'ynash, yugurish,,\n"
                    " velosipedda yurish va boshqa sport turlari uchun ham mos keladi",
                    "img_20.png", 1)

product20 = Product("Tommy Hifiger🧢", 200.000,
                    "Kepining beysbol kepkasi futbol o'ynash, yugurish,,\n"
                    " velosipedda yurish va boshqa sport turlari uchun ham mos keladi",
                    "img_21.png", 1)

product21 = Product("Kulirang", 130.000,
                    "Ayollar kiyimi savdosi - romollar. Ko'proq ko ... Opa singillarimiz uchun \n"
                    " hijob ro'mollar. Yangi 99 ... sharf romollar bo'lim: Ayollar kiyimi · sharf romollar bor...",
                    "img_22.png", 1)

product22 = Product("Romol_Oq⚪", 100.000,
                    "Kepining beysbol kepkasi futbol o'ynash, yugurish,,\n"
                    " velosipedda yurish va boshqa sport turlari uchun ham mos keladi",
                    "img_23.png", 1)

product23 = Product("Romol_Qora⚫", 90.000,
                    "Kepining beysbol kepkasi futbol o'ynash, yugurish,,\n"
                    " velosipedda yurish va boshqa sport turlari uchun ham mos keladi",
                    "img_24.png", 1)

product24 = Product("Prada", 900.000,
                    "Re-Edition shearling mini bag"
                    "The cosy shearling construction of this Prada bag lends to its wintry feel. "
                    "Gold-tone accents offer the accessory a refined touch, while three,"
                    " interchangeable straps allow for versatile styling.",
                    "img_25.png", 1)

product25 = Product("Monnalisa", 900.000,
                    "Discover the latest collections of girl bags, backpacks for ,"
                    "leisure or for school, designed by Monnalisa. Original design to be always trendy and at the ...",
                    "img_26.png ", 1)

product26 = Product("Saint Laurent", 800.000,
                    "Re-Edition shearling mini bag"
                    "The cosy shearling construction of this Prada bag lends to its wintry,"
                    " feel. Gold-tone accents offer the accessory a refined touch, while,"
                    " three interchangeable straps allow for versatile styling.",
                    "img_27.png", 1)

product27 = Product("Alexender", 700.000,
                    "medium Wangloc rhinestone-embellished clutch bag,"
                    "Looking to take it up a gear? Time to engage the clutch, specifically, this ,"
                    "Wangloc clutch bag from Alexander Wang with its crystal embellishments ,"
                    "and rectangular shape. No stalling here, just style.",
                    "img_28.png", 1)

product28 = Product("Kurtka🧥", 700.000,
                    "Inspired by the 1996 version, the Retro Nuptse jacket is a durable style known ,"
                    "for its lofty 700-fill down construction and for having a sleek and stowable ,"
                    "hood at the rear. The design appears in a full-black tone and ,"
                    "is detailed with the brand's logo at the chest and at the rear.",
                    "img_29.png", 1)

product29 = Product("Palto🧥", 900.000,
                    "sheepskin biker jacketsand beige sheepskin double-breasted ,"
                    "button fastening buttoned cuffs belted waist classic lapelsMade in Italy",

                    "img_30.png", 1)

product30 = Product("Jemper", 200.000,
                    "Qizlar uchun bolalar jumper - bu faol kichkina modaistlar uchun maxsus ,"
                    "yaratilgan engil va qulay kiyim. Ushbu jumper odatda sovuq oylarda qulaylikni ta'minlash,"
                    " uchun paxta yoki jun kabi yumshoq va issiq materialdan tayyorlanadi.Odatda ,"
                    "kichik modaistlar yoqtiradigan yorqin va jozibali dizaynga ega. Qizlar uchun bolalar jumperlari,"
                    " naqshlar, aplikatsiyalar, kashtado'zlik yoki boshqa bezak,"
                    " elementlari bilan bezatilgan bo'lib, ularga o'ziga xos uslubni beradi.",
                    "img_31.png", 1)

product31 = Product("Brunello👖", 900.000,
                    "virgin wool-blend trousersThese Brunello Cucinelli trousers are made from,"
                    " a blend of virgin wool and silk, while a pressed crease adds a refined finish.Made in Italy",
                    "img_32.png", 1)

product32 = Product("Zegna👖", 900.000,
                    "tapered-leg track-pantsnavy blue wool elasticated waistband,"
                    " pressed crease two side slit pockets rear welt pocket tapered leg",
                    "img_33.png", 1)

product33 = Product("Polo Ralph👖", 900.000,
                    "mid-rise straight-leg trousers",
                    "img_34.png", 1)

product34 = Product("Sartoria👖", 900.000,
                    "tapered-leg track-pantsnavy blue wool elasticated waistband,"
                    " pressed crease two side slit pockets rear welt pocket tapered leg",
                    "img_35.png", 1)

product35 = Product("Loro Piana-k👟", 800.000,
                    "Мужская обувь люкс качества от Loro Piana . Кроссовки на шнурке. Логотип бренда на заднике. Белая подошва.",
                    "img_36.png", 1)

product36 = Product("Adidas-k👟", 700.000,
                    "adidas Kids’ Campus 00s sneakers are a Y2K take on the ‘80s original. Retaining the suede upper and,\
                     contrasting leather 3-Stripes at the sidewall, this pair is rendered in a neutral Black White Gum colourway.",
                    "img_37.png", 1)

product37 = Product("Nike-k👟", 900.000,
                    "Released in 1985, the Air Jordan 1 Low stands out for its bold colour-block design. This pair comes in the brand’s “Panda”,"
                    " black and white colourway and features branded details throughout. Nike’s signature swoosh,"
                    " appears prominently on the sides while the Jumpman logo and the line's",
                    "img_38.png", 1)

product38 = Product("Gucci-k👟", 800.000,
                    "A branding-focused design, these Gucci sneakers ,"
                    "boast the house's signature GG Supreme canvas. This detailing is embellished,"
                    " with brown and blue leather panels for an effortless finish.",
                    "img_39.png", 1)

product39 = Product("Oq Popka", 300.000,
                    "【Mutlaq qiymat】- Ikki tomonlama mustahkam fermuar bilan jihozlangan mashhur,"
                    " sport dizayni bilan mukammal sayohat aksessuari, ayniqsa sayohat,,"
                    " fitnes, golf, basketbol va futbol ixlosmandlari uchun.",
                    "img_40.png", 1)

product40 = Product("Qora Popka", 420.000,
                    "Mahsulotning xususiyatlari va qo'llanilishi erkaklar uchun,"
                    " moda ko'p qirrali elkama-sumkasi ko'p funktsiyali xoch sumkasi oddiy shaxsiy kundalik sumkasi",

                    "img_41.png", 1)

product41 = Product("Boss Kidswear👟", 9000.000,
                    "This BOSS Kidswear tracksuit set is crafted from a cotton blend,"
                    " that’s naturally breathable against the skin. It comprises a coordinating,"
                    " zip-up jacket and track pants adorned with stripe trims and subtle logo lettering.",
                    "img_42.png", 1)

product42 = Product("Billionarie", 4000.000,
                    "This BOSS Kidswear tracksuit set is crafted from a cotton blend,"
                    " that’s naturally breathable against the skin. It comprises a coordinating,"
                    " zip-up jacket and track pants adorned with stripe trims and subtle logo lettering.",
                    "img_43.png", 1)

product43 = Product("Prada", 800.000,
                    "Designed to stand the test of time, this T-shirt from Prada showcases a minimal\
                     design. Simply punctuated by a tonal embroidered logo to the chest, \
                     this crew-neck piece proves itself a versatile casual staple.",
                    "img_44.png", 1)

product44 = Product("Calvin", 600.000,
                    "logo-print cotton T-shirt",
                    "img_45.png", 1)

product45 = Product("Boss", 1000.000,
                    "The model  1.88 m.The model is also styled with LEMAIRE straight-leg,"
                    " cotton jeans, AMI Paris Lace-Up Low-Top Sneakers, ARCS Sharp buckle-detail crossbody bag",
                    "img_46.png", 1)

product46 = Product("Moschino", 800.000,
                    "black/white silk blend Top: contrasting trim embroidered logo to the front notched ,"
                    "lapels chest patch pocket front button fastening short sleeves straight hem Shorts: high waist,"
                    " elasticated waistband rear patch pocket straight hem",
                    "img_47.png", 1)

product47 = Product("Trussardi", 400.000,
                    "beige/white cotton logo print at the leg belt loops elasticated waistband front,"
                    " button and zip fastening two side inset pockets two rear welt pockets straight leg elasticated cuffs",
                    "img_48.png", 1)

product48 = Product("Oltin Gerbi", 120.000,
                    "Erkaklar uchun oq kepka O'zbekistonning oltin gerbi bilan - stil va vatandoshlikdagi kepi, ,"
                    "O'zbekistonga bo'lgan aloqangizni ifodalovchi aksessuar. Sifatli materiallardan ishlab chiqarilgan,"
                    " u sizga qulay ta'sir va davomiylilik ta'minlaydi. Oltin rangda ishlangan O'zbekiston "
                    "gerbi kepkaga yorqinlik va joziba bag'ishlaydi. Ushbu kepka har kuni ishlatish uchun ham,"
                    " mahsulotdan foydalanishga yoki maxsus tadbirlarga mos keladi",
                    "img_49.png", 1)

product49 = Product("Kepka-Art", 200.000,
                    "Toshkentda “Kiyim_Botidan” bozoridan qalpoq va beysbolkalarni xarid qilish oson ,"
                    "va qulay. Sababi bizda narxlar juda past. O'zbekiston bo'ylab yetkazib berish xizmati "
                    ",mavjud! Ayollar va erkaklar uchun qaysi brendning zamonaviy, zamonaviy qalpoqlarini ,"
                    "afzal ko'rasiz? Jordan, Gucci, Calvin Klein, Louis Vuitton, Adidas, Nike, Nyu-York, Puma,,"
                    " Loro Piano, New Era, Tommy Hilfiger - bo'lib-bo'lib barcha brendlarning moda qalpoqlari.,"
                    " Shuningdek, Caps bo'limida siz turli xil nashrlar bilan tvid qopqoqlarni ,"
                    "osongina topishingiz mumkin. Hoziroq buyurtma bering va savdolashing!",
                    "img_50.png", 1)

product50 = Product("Body", 70.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_52.png", 1)


product51 = Product("Kombenizon", 120.000,
                    "Quyoncha chaqaloqlar uchun paxtadan tayyorlangan bolalar,"
                    " kombinezonlari,yangi tug'ilgan chaqaloqlar va 1.5 - 2 yoshgacha bo'lgan bolalar,"
                    " uchun mos keladi. Bolalar kombinezonlari chaqalog'ingiz uchun qulay va amaliy kiyimdir.,"
                    " Quyon quloqlari bilan yoqimli va oqlangan kombinezonda bolangiz doimo diqqat markazida,"
                    " bo'ladi. Barcha modellar chaqaloqning nozik terisini bezovta qilmaydigan yumshoq ,"
                    "va nafas oladigan paxta materialidan tayyorlangan.",
                    "img_53.png", 1)

product52 = Product("Qishki Koylak", 200.000,
                    "Material: Paxta, yumshoq va qulay, chaqalog'ingizga yumshoq iliq tuyg'u ,"
                    "bering.Paketga qo'shish: 1PC RomperHajmi: Iltimos, despription-ga murojaat ,"
                    "qiling. 0-2 yoshdagi bolalar uchun sovg'a.",
                    "img_54.png", 1)


product53 = Product("Kuzgi Koylak", 200.000,
                    "Ayiq yangi tug'ilgan tuqqan ko'ylak Paxta kuzgi bahorgi chaqaloq,"
                    " romperi Kichkintoylar o'g'il bolalar kiyimlari Go'daklar bir,"
                    " bo'lakli bolalar tulumlari uy dam olish kiyimlari",
                    "img_55.png", 1)


product54 = Product("Oq", 70.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_56.png", 1)


product55 = Product("Sariq", 70.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_57.png", 1)


product56 = Product("Qora", 100.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_58.png", 1)


product57 = Product("Sariq", 120.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_59.png", 1)


product58 = Product("Kok", 120.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_60.png", 1)


product59 = Product("Qora", 120.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_61.png", 1)


product60 = Product("Kurtka🧥_bola", 300.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_62.png", 1)


product61 = Product("Palto🧥_bola", 250.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_63.png", 1)


product62 = Product("Jemper_bola", 200.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_64.png", 1)


product63 = Product("Burbery_bola", 100.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_65.png", 1)


product64 = Product("Tullen_bola", 300.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " qizlar bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_66.png", 1)


product65 = Product("Sandro_bola", 150.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_67.png", 1)


product66 = Product("Jemper_bola", 200.000,
                    "Kichkintoy bodisi, klassik jentlmen uslubidaYangi Bello Joy kolleksiyasidan,"
                    " o'g'il bolalar uchun nafis kombinezonlarModel tugmalar bo'yin zonaga va undan keyin ,"
                    "shimning ichki tikuvlari bo'ylab joylashgan",
                    "img_68.png", 1)
