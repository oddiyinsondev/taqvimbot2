from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



Menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='π Taqvim', callback_data='ramazon'), InlineKeyboardButton(text='Sura va hadis', callback_data='malumot')],
        [InlineKeyboardButton(text="π Ma'lumotnoma", callback_data='kitob'), InlineKeyboardButton(text='Xayriya guruh', url='https://t.me/alif_xayriya')],
        [InlineKeyboardButton(text="πRamazon xaqida", callback_data="xaqida")]
    ]
)

kitobim = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kuchsiz bo'lsangiz"), KeyboardButton(text="Safarda oqiladigan duo")],
        [KeyboardButton(text="Jahldor bo'lsangiz"), KeyboardButton(text="Iymon zaiflashsa")],
        [KeyboardButton(text="baxtsiz bo'lsangiz"), KeyboardButton(text="Gunox qilgan bolsangiz")],
        [KeyboardButton(text="Tashvishda bo'lsangiz"), KeyboardButton(text="π ASOSIY MENYU")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


viloyat = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Toshkent', callback_data='toshkent'),InlineKeyboardButton(text='Jizzax', callback_data='jizzax')],
        [InlineKeyboardButton(text="Farg'ona", callback_data='fargona'),InlineKeyboardButton(text='Andijon', callback_data='andijon')],
        [InlineKeyboardButton(text='Buxoro', callback_data='buxoro'),InlineKeyboardButton(text='Namangan', callback_data='namangan')],
        [InlineKeyboardButton(text='Navioy', callback_data='navioy'),InlineKeyboardButton(text='Qashqadaryo', callback_data='qarshi')],
        [InlineKeyboardButton(text='Samarqand', callback_data='samarqand'),InlineKeyboardButton(text='Sirdaryo', callback_data='sirdaryo')],
        [InlineKeyboardButton(text='Surxondaryo', callback_data='termiz'),InlineKeyboardButton(text='Xorazm', callback_data='xorazm')],
        [InlineKeyboardButton(text="Qoraqalpog'iston", callback_data='nukus'), InlineKeyboardButton(text='π ASOSIY MENYU', callback_data='asosiy')]
    ]
)

andijon = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Andijon'), KeyboardButton(text='Namoz taqvim Andijon')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

qarshi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Qashqadaryo'), KeyboardButton(text='Namoz taqvim Qashqadaryo')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


surxon = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Surxandaryo'), KeyboardButton(text='Namoz taqvim Surxandaryo')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
jizzax = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Jizzax'), KeyboardButton(text='Namoz taqvim Jizzax')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
navoiy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Navoiy'), KeyboardButton(text='Namoz taqvim Navoiy')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

samarqand = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Samarqand'), KeyboardButton(text='Namoz taqvim Samarqand')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

fargona = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Fargona'), KeyboardButton(text='Namoz taqvim Fargona')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

xorazm = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Xorazm'), KeyboardButton(text='Namoz taqvim Xorazm')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

namangan = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Namangan'), KeyboardButton(text='Namoz taqvim Namangan')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

sirdaryo = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Sirdaryo'), KeyboardButton(text='Namoz taqvim Sirdaryo')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

buxoro = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Buxoro'), KeyboardButton(text='Namoz taqvim Buxoro')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

qaraqalpoq = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Qaraqalpoqiston'), KeyboardButton(text='Namoz taqvim Qaraqolpoqiston')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

toshkent = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ramazon taqvim Toshkent'), KeyboardButton(text='Namoz taqvim Toshkent')],
        # [KeyboardButton(text='Ramazon taqvim kunlik'), KeyboardButton(text='Namoz vaqt kunlik')],
        [KeyboardButton(text="π€² duolar"),KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


suralar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Fotixa surasi"), KeyboardButton(text="Qunut duosi")],
        [KeyboardButton(text="Kavsar surasi"), KeyboardButton(text="π€² DUO")],
        [KeyboardButton(text="Azon duosi"), KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


xazina = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="π Π ΡΠ·Π°Π΄ΠΎΡΠ»Π°Ρ ΡΡΡΠ½ ΡΡΡΡΠ°Π±Π°Ρ"), KeyboardButton(text="Π Π°ΠΌΠ°Π·ΠΎΠ½Π½ΠΈ ΡΡ ΡΠ°Π·ΠΈΠ½Π°")],
        [KeyboardButton(text="ΡΠ°ΡΠΎΡΠ°Ρ ΡΠ°ΠΊΠΈΠ΄Π°")],
        [KeyboardButton(text="Π Π°ΠΌΠ°Π·ΠΎΠ½"), KeyboardButton(text='π ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

