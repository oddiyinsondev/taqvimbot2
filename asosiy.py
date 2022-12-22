from tokken import TOKEN
import logging
from buttons import  Menu,viloyat, andijon,samarqand,sirdaryo,surxon,xorazm,toshkent,qaraqalpoq,qarshi,buxoro,namangan,navoiy,jizzax,fargona,kitobim,suralar,xazina
from aiogram import  Bot, executor, types, Dispatcher
from kochirma import asos6, asos2, asos3, asos4, asos5, asos1, asos7 , dok, suralar1,suralar2,suralar3,suralar4,suralar5

# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO) 


@dp.message_handler(commands=['start'], state="*")
async def boshi(message: types.Message):
    odi = message.from_user.first_name
    id = message.from_user.id
    await message.answer_photo(photo = "https://aniq.uz/photos/news/Zu4hV5HMR510WqB.jpeg",caption=f"Assalom alaykum rahmatillohu va barakatuh {odi}\nBizning bot sizga yordam berishga tayor\n/help", reply_markup=Menu)
    


@dp.message_handler(commands=['help'], state="*")
async def yordam(message: types.Message):
    await message.answer_photo(photo = "https://i.ytimg.com/vi/u1igG-2U6hw/maxresdefault.jpg",caption=f"Bot bo'yicha murojarlar va yangilikla bo'lsa\nNickname: @salihxon\nIsm: Shohruhbek")
    

@dp.callback_query_handler(text_contains='ramazon', state="*")
async def ramazon(call: types.CallbackQuery):
     await call.answer(cache_time=5)
     await call.message.delete()
     await call.message.answer_photo(photo="https://zamin.uz/uploads/posts/2021-04/1617909004_01.jpg", caption="o'zingiz yashayotgan mintaqangizni tanlang", reply_markup=viloyat)


@dp.callback_query_handler(text_contains='asosiy', state='*')
async def asosy_menyu(call: types.CallbackQuery):
    await call.answer(cache_time=8)
    await call.message.delete()
    await call.message.answer_photo(photo = "https://aniq.uz/photos/news/Zu4hV5HMR510WqB.jpeg",caption=f"Asosiy menyuga xush kelibsiz\n Yordam bo'yicha muroja bo'lsa\n/help", reply_markup=Menu)


@dp.callback_query_handler(text_contains ='kitob', state='*')
async def kitob(call: types.CallbackQuery):
    await call.answer(cache_time=8)
    await call.message.delete()
    await call.message.answer(f"Ozingizni tashvishgan solgan savolga javob olishingizga ishonamiz 🤲",reply_markup=kitobim)

@dp.callback_query_handler(text_contains='xaqida', state="*")
async def ramazon(call: types.CallbackQuery):
     await call.answer(cache_time=5)
     await call.message.delete()
     await call.message.answer_photo(photo="https://zamin.uz/uploads/posts/2021-04/1617909004_01.jpg", caption="Ramazon muborak", reply_markup=xazina)


@dp.message_handler(text="🚞 ASOSIY MENYU", state='*')
async def asosiy_menu(message: types.Message):
    await message.answer_photo(photo = "https://aniq.uz/photos/news/Zu4hV5HMR510WqB.jpeg",caption=f"Asosiy menyuga xush kelibsiz\n Yordam bo'yicha muroja bo'lsa\n/help", reply_markup=Menu)


@dp.callback_query_handler(text_contains='malumot',state='*')
async def namoz_vaqt(call: types.CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.delete()
    await call.message.answer(" 🤲 SURALAR", reply_markup=suralar)


# @dp.callback_query_handler(text_contains='guruh', state='*')
# async def guruh(call: types.CallbackQuery):
#     guruh = 'https://t.me/alif_xayriya'
#     await call.message.answer(f"Bizning guruhga xush kelibsiz {guruh}")



@dp.callback_query_handler(text_contains = 'andijon')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=andijon)


@dp.callback_query_handler(text_contains = 'toshkent')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=toshkent)

@dp.callback_query_handler(text_contains = 'jizzax')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=jizzax)

@dp.callback_query_handler(text_contains = 'fargona')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=fargona)

@dp.callback_query_handler(text_contains = 'buxoro')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=buxoro)

@dp.callback_query_handler(text_contains = 'namangan')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=namangan)

@dp.callback_query_handler(text_contains = 'qarshi')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=qarshi)

@dp.callback_query_handler(text_contains = 'sirdaryo')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=sirdaryo)

@dp.callback_query_handler(text_contains = 'xorazm')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=xorazm)

@dp.callback_query_handler(text_contains = 'nukus')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=qaraqalpoq)

@dp.callback_query_handler(text_contains = 'termiz')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=surxon)

@dp.callback_query_handler(text_contains = 'samarqand')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=samarqand)

@dp.callback_query_handler(text_contains = 'navioy')
async def anjon(call: types.CallbackQuery):
    await call.answer(cache_time=15)
    await call.message.delete()
    await call.message.answer("Sizning so'rovingiz bajarildi", reply_markup=navoiy)


@dp.message_handler(text='Ramazon taqvim Andijon')
async def ramazon_anjon(message: types.Message):
    await message.answer_photo(photo=open("img/anjon ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")


@dp.message_handler(text='Ramazon taqvim Qashqadaryo')
async def ramazon_qashqadaryo(message: types.Message):
    await message.answer_photo(photo=open("img/qashqadaryo ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
    
    
@dp.message_handler(text='Ramazon taqvim Surxandaryo')
async def ramazon_surxondaryo(message: types.Message):
    await message.answer_photo(photo=open("img/surxondaryo ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
    

@dp.message_handler(text='Ramazon taqvim Jizzax')
async def ramazon_jizzax(message: types.Message):
    await message.answer_photo(photo=open("img/jizzax ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
    

@dp.message_handler(text='Ramazon taqvim Navoiy')
async def ramazon_navoiy(message: types.Message):
    await message.answer_photo(photo=open("img/navoiy ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")


@dp.message_handler(text='Ramazon taqvim Samarqand')
async def ramazon_samarqand(message: types.Message):
    await message.answer_photo(photo=open("img/samrqand ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
    

@dp.message_handler(text='Ramazon taqvim Fargona')
async def ramazon_fargona(message: types.Message):
    await message.answer_photo(photo=open("img/fargona ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
    

@dp.message_handler(text='Ramazon taqvim Xorazm')
async def ramazon_xorazm(message: types.Message):
    await message.answer_photo(photo=open("img/xorazm ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
    

@dp.message_handler(text='Ramazon taqvim Namangan')
async def ramazon_namangan(message: types.Message):
    await message.answer_photo(photo=open("img/namngan ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
    

@dp.message_handler(text='Ramazon taqvim Sirdaryo')
async def ramazon_sirdaryo(message: types.Message):
    await message.answer_photo(photo=open("img/sirdaryo ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
    

@dp.message_handler(text='Ramazon taqvim Buxoro')
async def ramazon_buxoro(message: types.Message):
    await message.answer_photo(photo=open("img/buxoro ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")


@dp.message_handler(text='Ramazon taqvim Qaraqalpoqiston')
async def ramazon_qaraqolpoq(message: types.Message):
    await message.answer_photo(photo=open("img/qaraqolpoq ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")


@dp.message_handler(text='Ramazon taqvim Toshkent')
async def ramazon_toshkent(message: types.Message):
    await message.answer_photo(photo=open("img/toshkent ramazon.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
      

@dp.message_handler(text='Namoz taqvim Toshkent')
async def namoz_toshkent(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/tosh_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
      

@dp.message_handler(text='Namoz taqvim Qashqadaryo')
async def namoz_qarshi(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/qarshi_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")


@dp.message_handler(text='Namoz taqvim Surxandaryo')
async def namoz_surxandaryo(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/su.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")


@dp.message_handler(text='Namoz taqvim Jizzax')
async def namoz_jizzax(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/jizzah_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

@dp.message_handler(text='Namoz taqvim Navoiy')
async def namoz_navoiy(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/navoy_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

@dp.message_handler(text='Namoz taqvim Samarqand')
async def namoz_samarqand(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/samarq_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

@dp.message_handler(text='Namoz taqvim Fargona')
async def namoz_fargona(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/fargonna_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

@dp.message_handler(text='Namoz taqvim Xorazm')
async def namoz_khorezm(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/xorazm namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

@dp.message_handler(text='Namoz taqvim Namangan')
async def namoz_namangan(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/namangan_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

@dp.message_handler(text='Namoz taqvim Sirdaryo')
async def namoz_sirdaryo(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/sirdar_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

@dp.message_handler(text='Namoz taqvim Buxoro')
async def namoz_buxoro(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/buxorro_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

@dp.message_handler(text='Namoz taqvim Qaraqalpoqiston')
async def namoz_toshkent(message: types.Message):
    await message.answer_photo(photo=open("img/rasm/qarqolpog_namoz.jpg", "rb"), caption="🤲 Бу кунда Аллоҳ дуоларимизни ижобат, фарзандларимизга салоҳият, ибодатларимизга гўзаллик, ризқимизга барака берсин! Аллоҳнинг паноҳида бўлинг")
   

"""kunlik taqvim qoldi 
              json yasash kerak!"""

@dp.message_handler(text_contains="Gunox qilgan bolsangiz")
async def mat(message: types.Message):
    G = asos6
    await message.answer_photo(photo="https://i.ytimg.com/vi/CRSYEcTNG0Y/mqdefault.jpg",caption=f"{G}")

@dp.message_handler(text_contains="Kuchsiz bo'lsangiz")
async def mati(message: types.Message):
    G = asos1
    await message.answer_photo(photo="https://i.ytimg.com/vi/CRSYEcTNG0Y/mqdefault.jpg",caption=f"{G}")

@dp.message_handler(text_contains="Jahldor bo'lsangiz")
async def mativ(message: types.Message):
    G = asos7
    await message.answer_photo(photo="https://i.ytimg.com/vi/CRSYEcTNG0Y/mqdefault.jpg",caption=f"{G}")

@dp.message_handler(text_contains="baxtsiz bo'lsangiz")
async def mativa(message: types.Message):
    G = asos4
    await message.answer_photo(photo="https://i.ytimg.com/vi/CRSYEcTNG0Y/mqdefault.jpg",caption=f"{G}")

@dp.message_handler(text_contains="Tashvishda bo'lsangiz")
async def mativat(message: types.Message):
    G = asos5
    await message.answer_photo(photo="https://i.ytimg.com/vi/CRSYEcTNG0Y/mqdefault.jpg",caption=f"{G}")

@dp.message_handler(text_contains="Iymon zaiflashsa")
async def mativats(message: types.Message):
    G = asos3
    await message.answer_photo(photo="https://i.ytimg.com/vi/CRSYEcTNG0Y/mqdefault.jpg",caption=f"{G}")

@dp.message_handler(text_contains="Safarda oqiladigan duo")
async def mativatsiya(message: types.Message):
    G = asos2
    await message.answer_photo(photo="https://i.ytimg.com/vi/CRSYEcTNG0Y/mqdefault.jpg",caption=f"{G}")

@dp.message_handler(text_contains="🤲 duolar")
async def duolar(message: types.Message):
    await message.answer_photo(photo=open("img/ramazonduo.jpg", "rb"), caption=f"{dok}")

@dp.message_handler(text_contains="Fotixa surasi")
async def fotixa(message: types.Message):
    mad = suralar1
    await message.answer_photo(photo=open("img/duo.jpeg", "rb"),caption=f"{mad}")

@dp.message_handler(text_contains="Qunut duosi")
async def qunt(message: types.Message):
    mad = suralar2
    await message.answer_photo(photo=open("img/duo.jpeg", "rb"),caption=f"{mad}")

@dp.message_handler(text_contains="Kavsar surasi")
async def kavsar(message: types.Message):
    mad = suralar3
    await message.answer_photo(photo=open("img/duo.jpeg", "rb"),caption=f"{mad}")

@dp.message_handler(text_contains="🤲 DUO")
async def duo(message: types.Message):
    mad = suralar4
    await message.answer_photo(photo=open("img/duo.jpeg", "rb"),caption=f"{mad}")

@dp.message_handler(text_contains="Azon duosi")
async def Azon(message: types.Message):
    mad = suralar5
    await message.answer_photo(photo=open("img/duo.jpeg", "rb"),caption=f"{mad}")

@dp.message_handler(text_contains="🌙 Рўзадорлар учун хушхабар")
async def rozador(message: types.Message):
    await message.answer_video(video=open("img/Shayx Muhammad Sodiq ro'za haqida.mp4", "rb"),caption=f"🌙 Рўзадорлар учун хушхабар\nШайх Муҳаммад Содиқ Муҳаммад Юсуф ҳазратлари\nЯқинларингизга ҳам улашинг!\n@oddiy_yangi_bot")

@dp.message_handler(text_contains="Рамазонни уч хазина")
async def xazinalar(message: types.Message):
    await message.answer_photo(photo=open("img/xazina.jpg", "rb"),caption=f"Рамазонни уч хазина билан кутиб олинг\n1 - Ким тасбеҳни давомий айтиб юрса, қалби енгил тортади.\n2 - Ким ҳамду санони давомий айтса, яхшиликлар кетма-кет келади.\n3 - Ким истиғфорда давомий бўлса, яхшилик эшиклари очилаверади.")

@dp.message_handler(text_contains="Рамазон")
async def ramozon_xazina(message: types.Message):
    await message.answer_photo(photo=open("img/exson.jpg", "rb"),caption=f"🤲")

@dp.message_handler(text_contains="тахорат хакида")
async def taxorat(message: types.Message):
    await message.answer_video(video=open("img/data.mp4", "rb"))


if __name__ == '__main__':
    executor.start_polling(dp, allowed_updates=True)