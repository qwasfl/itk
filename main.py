
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import asyncio

class CountdownStates(StatesGroup):
    countdown = State()

API_TOKEN = '7936983697:AAHR77UeI764eo-l_3TY3HhFJhkYl2wgOb4'  # Замените на ваш токен

logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Поисковые ситемы", callback_data='button1')
    button2 = types.InlineKeyboardButton("Скоро", callback_data='button2')
    keyboard.add(button1, button2,)

    photo_path = 'img/1.png'  # Замените на имя вашего файла

    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, 
                                 photo=photo, 
                                 caption="Привет! Этот бот был создан qwasfl(максимом) \nчтобы ты узнал о <code>Интертене больше</code>", 
                                 reply_markup=keyboard, 
                                 parse_mode='HTML')
    await message.delete()


@dp.message_handler(lambda message: message.text != "/start")
async def handle_invalid_command(message: types.Message):
    from io import BytesIO

    # Открываем изображение
    with open(r'C:\Users\woriv\OneDrive\Рабочий стол\школа бот ИТК\img\eror404.png', 'rb') as photo_file:
        photo_bytes = BytesIO(photo_file.read())

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Перейти на главную", callback_data='button1')
    keyboard.add(button1)

    # Отправляем сообщение с изображением
    sent_message = await bot.send_photo(chat_id=message.chat.id, 
                                         photo=photo_bytes, 
                                         caption="Начинается обратный отсчет с 5", 
                                         reply_markup=keyboard, 
                                         parse_mode='HTML')

    # Обратный отсчет от 5 до 1
    for i in range(5, 0, -1):
        await asyncio.sleep(1)  # Ждать 1 секунду
        # Редактируем предыдущее сообщение с обновленным текстом
        await bot.edit_message_caption(chat_id=message.chat.id, 
                                        message_id=sent_message.message_id, 
                                        caption=f"Осталось {i} секунд...", 
                                        reply_markup=keyboard)

    # После обратного отсчета отправляем приветственное сообщение
    await sent_message.delete()
    await send_welcome(message)






@dp.callback_query_handler(lambda c: c.data in ['start'])
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Поисковые ситемы", callback_data='button1')
    button2 = types.InlineKeyboardButton("Скоро", callback_data='button2')
    keyboard.add(button1, button2,)

    photo_path = 'img/1.png'  # Замените на имя вашего файла

    with open(photo_path, 'rb') as photo:
        await bot.send_photo(callback_query.from_user.id, 
                                 photo=photo, 
                                 caption="Привет! Этот бот был создан qwasfl(максимом) \nчтобы ты узнал о <code>Интертене больше</code>", 
                                 reply_markup=keyboard, 
                                 parse_mode='HTML')

@dp.callback_query_handler(lambda c: c.data in ['button1', 'button2'])
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == 'button1':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    
        # Отправляем новое сообщение с другой фотографией, текстом и кнопками
        new_keyboard = types.InlineKeyboardMarkup()
        new_button1 = types.InlineKeyboardButton("1. Что такое поисковая система интернета?", callback_data='1.1')
        new_button2 = types.InlineKeyboardButton("2. Типы поисковых систем", callback_data='1.2')
        new_button3 = types.InlineKeyboardButton("3. Популярные поисковые системы в России", callback_data='1.3')
        new_button4 = types.InlineKeyboardButton("4. Популярные поисковые системы Зарубежом", callback_data='1.4')
        new_keyboard.add(new_button1, new_button2, new_button3, new_button4)

        new_photo_path = 'img/2.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="Выберете:", 
                                reply_markup=new_keyboard)
    if callback_query.data == 'button2':
        await bot.answer_callback_query(callback_query.id, text="СКОРО")


@dp.callback_query_handler(lambda c: c.data in ['1.1', '1.2', '1.3','1.4'])
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == '1.1':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    
        # Отправляем новое сообщение с другой фотографией, текстом и кнопками
        next_keyboard = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton("Назад", callback_data='button1')
        menu1_button = types.InlineKeyboardButton("В начало", callback_data='start')
        next_button = types.InlineKeyboardButton("Далее", callback_data='1.2')
        next_keyboard.add(back_button, menu1_button, next_button)

        new_photo_path = 'img/2.1.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="Глава 1: Что такое поисковая система интернета Поисковая система — это программное обеспечение \n с веб-интерфейсом, которое позволяет искать информацию в интернете. Все поисковые системы имеют общую черту: они расположены на мощных серверах \n и подключены к эффективным каналам связи. \n Поисковые системы также называют информационно-поисковыми (ИПС). \n Для поиска информации пользователь формулирует поисковый запрос. \n На основе этого запроса поисковая система генерирует страницу результатов поиска. \n Эта выдача может включать различные типы файлов, такие как веб-страницы, изображения и видео.",
                                reply_markup=next_keyboard)
    if callback_query.data == '1.2':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        next_keyboard = types.InlineKeyboardMarkup()
        back1_button = types.InlineKeyboardButton("Назад", callback_data='1.1')
        menu_button = types.InlineKeyboardButton("Меню", callback_data='button1')
        next_button = types.InlineKeyboardButton("Далее", callback_data='1.3')
        next_keyboard.add(back1_button, menu_button, next_button)

        new_photo_path = 'img/2.2.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="Глава 2: Типы поисковых систем По методам поиска и обслуживания выделяют четыре типа\n поисковых систем: системы, использующие поисковых роботов; системы, управляемые человеком; гибридные системы; \nмета-системы. Архитектура поисковой системы включает поискового робота, сканирующего \nсайты интернета, индексатора, обеспечивающего быстрый поиск, \nи поисковика — графического интерфейса для работы пользователя. Цель поисковой системы — находить документы, содержащие ключевые слова или слова, связанные с ключевыми словами.\n Чем больше документов, релевантных запросу пользователя, система возвращает, тем лучше она работает.",
                                reply_markup=next_keyboard)
    if callback_query.data == '1.3':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        next_keyboard = types.InlineKeyboardMarkup()
        Yandex_button = types.InlineKeyboardButton("Яндекс", callback_data='Yandex')
        Google_button = types.InlineKeyboardButton("Google", callback_data='Google')
        Rambler_button = types.InlineKeyboardButton("Rambler", callback_data='Rambler')

        back1_button = types.InlineKeyboardButton("Назад", callback_data='1.2')
        menu_button = types.InlineKeyboardButton("Меню", callback_data='button1')
        next_button = types.InlineKeyboardButton("|", callback_data='nex3333333t')
        next_keyboard.add(Yandex_button, Google_button, Rambler_button, back1_button, next_button, menu_button)

        new_photo_path = 'img/2.3.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="Популярные поисковые системы в России:\n- Яндекс\n- Google\n- Rambler",
                                reply_markup=next_keyboard)
    if callback_query.data == '1.4':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        next_keyboard = types.InlineKeyboardMarkup()
        Yahoo_button = types.InlineKeyboardButton("AltaVista и Yahoo!", callback_data='Yahoo')
        Bing_button = types.InlineKeyboardButton("Bing", callback_data='Bing')
        Google_en_button = types.InlineKeyboardButton("Google", callback_data='Google_en')

        back1_button = types.InlineKeyboardButton("Назад", callback_data='1.3')
        menu_button = types.InlineKeyboardButton("Меню", callback_data='button1')
        next_button = types.InlineKeyboardButton("|", callback_data='nex3333333t')
        next_keyboard.add(Yahoo_button, Google_en_button, Bing_button, back1_button, next_button, menu_button)

        new_photo_path = 'img/2.4.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="Популярные поисковые системы Зарубежом:\n- AltaVista и Yahoo!\n- Google\n- Bing",
                                reply_markup=next_keyboard)
            
@dp.callback_query_handler(lambda c: c.data in ['Yahoo'])
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == 'Yahoo':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        next_keyboard = types.InlineKeyboardMarkup()

        back1_button = types.InlineKeyboardButton("Назад", callback_data='1.4')
        menu_button = types.InlineKeyboardButton("Меню", callback_data='button1')
        next_button = types.InlineKeyboardButton("Далее", callback_data='Google_en')
        next_keyboard.add(back1_button, menu_button, next_button)

        new_photo_path = 'img/Yahoo.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="** AltaVista ** была поисковой системой в Интернете, основанной в 1995 году .\n Она стала одной из наиболее часто используемых ранних поисковых систем, но уступила позиции Google и была приобретена Yahoo !\n в 2003 году, который сохранил бренд, но основывал все запросы ** AltaVista ** на своей собственной поисковой системе . \n8 июля 2013 года сервис был закрыт Yahoo ! и с тех пор домен был перенаправлен на собственный поисковый сайт Yahoo!. \nСлово “AltaVista” образовано от слов, обозначающих “вид с высоты” в испанском языке (alta + vista). \nAltaVista — одна из старейших поисковых систем занимает одно из первых мест по объему документов — более 350 миллионов. AltaVista позволяет осуществлять простой и расширенный поиск. \n“Help” позволяет даже неподготовленным пользователям правильно составлять простые и сложные запросы. \nТекущий статус — активен.",
                                reply_markup=next_keyboard)
@dp.callback_query_handler(lambda c: c.data in ['Google_en'])
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == 'Google_en':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        next_keyboard = types.InlineKeyboardMarkup()

        back1_button = types.InlineKeyboardButton("Назад", callback_data='Yahoo')
        menu_button = types.InlineKeyboardButton("Меню", callback_data='1.4')
        next_button = types.InlineKeyboardButton("Далее", callback_data='Bing')
        next_keyboard.add(back1_button, menu_button, next_button)

        new_photo_path = 'img/Google_en.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="Эта система была создана как образовательный проект \nстудентами Стэнфордского университета (США) Ларри Пейджем и Сергеем Брином. \nВ 1996 году они разработали систему Back Rub Substation System, а в 1998 году на её основе создали систему Google. Google — это первый популярный англоязычный поисковик (79,65%), обрабатывающий 41 миллиард 345 миллионов запросов в месяц (доля рынка 62,4%), индексирующий более 25 миллиардов веб-страниц и способный находить информацию на 195 языках. Поддерживает поиск в документах форматов PDF, RTF, PostScript, Microsoft Word, Microsoft Excel, \nMicrosoft PowerPoint и других. Эта система была создана в качестве учебного проекта студентами Стэнфордского университета (США) Ларри Пэйджем и Сергеем Брином. В 1996 г. они разрабатывали ПС Back Ru. \nТекущий статус — активен.",
                                reply_markup=next_keyboard)
@dp.callback_query_handler(lambda c: c.data in ['Bing'])
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == 'Bing':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        next_keyboard = types.InlineKeyboardMarkup()

        next_button = types.InlineKeyboardButton("Перейти в начало", callback_data='start')
        next_keyboard.add(next_button)

        new_photo_path = 'img/Bing.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="Эта система была создана как образовательный проект \nстудентами Стэнфордского университета (США) Ларри Пейджем и Сергеем Брином. \nВ 1996 году они разработали систему Back Rub Substation System, а в 1998 году на её основе создали систему Google. Google — это первый популярный англоязычный поисковик (79,65%), обрабатывающий 41 миллиард 345 миллионов запросов в месяц (доля рынка 62,4%), индексирующий более 25 миллиардов веб-страниц и способный находить информацию на 195 языках. Поддерживает поиск в документах форматов PDF, RTF, PostScript, Microsoft Word, Microsoft Excel, \nMicrosoft PowerPoint и других. Эта система была создана в качестве учебного проекта студентами Стэнфордского университета (США) Ларри Пэйджем и Сергеем Брином. В 1996 г. они разрабатывали ПС Back Ru. \nТекущий статус — активен.",
                                reply_markup=next_keyboard) 



@dp.callback_query_handler(lambda c: c.data in ['Yandex'])
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == 'Yandex':
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
        next_keyboard = types.InlineKeyboardMarkup()

        back1_button = types.InlineKeyboardButton("Назад", callback_data='1.3')
        menu_button = types.InlineKeyboardButton("Меню", callback_data='button1')
        next_button = types.InlineKeyboardButton("Далее", callback_data='Google')
        next_keyboard.add(back1_button, menu_button, next_button)

        new_photo_path = 'img/Yandex.png'  # Замените на имя вашего нового файла

        with open(new_photo_path, 'rb') as new_photo:
            await bot.send_photo(callback_query.from_user.id, 
                                photo=new_photo, 
                                caption="Yandex — самая популярная отечественная поисковая система. Она начала работать в 1997 году и поддерживает собственный каталог интернет-ресурсов. \nТакже является лучшей поисковой системой для поиска иллюстраций. Англоязычная версия снабжена справочником интернет-ресурсов. \nОбладает развернутой системой формирования запроса. В частности, допускается ввод поискового предписания на естественном языке — \nв этом случае все необходимые расширения производятся автоматически. Помимо веб-страниц в формате HTML, Яндекс индексирует документы в форматах \nPDF (Adobe Acrobat), Rich Text Format (RTF), двоичных форматах Word (.doc), Excel (.xls),\n PowerPoint (.ppt), RSS (блоги и форумы) (рис. 3.1). \nТекущий статус — активен.",
                                reply_markup=next_keyboard)
            

@dp.callback_query_handler(lambda c: c.data in ['Google'])
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    next_keyboard = types.InlineKeyboardMarkup()

    back1_button = types.InlineKeyboardButton("Назад", callback_data='Yandex')
    menu_button = types.InlineKeyboardButton("Меню", callback_data='1.3')
    next_button = types.InlineKeyboardButton("Далее", callback_data='Rambler')
    next_keyboard.add(back1_button, menu_button, next_button)

    new_photo_path = 'img/Google.png'  # Замените на имя вашего нового файла

    with open(new_photo_path, 'rb') as new_photo:
        await bot.send_photo(callback_query.from_user.id, 
                            photo=new_photo, 
                            caption="Google — одна из самых популярных зарубежных поисковых систем, принадлежащая корпорации Google Inc.\n Она занимает первое место в мире по количеству запросов (рис. 3.2). В России Google предлагает русскоязычный интерфейс, \nчто удобно для пользователей. Главная особенность Google — алгоритм определения релевантности документа, анализирующий \nссылки на ресурс с других страниц. Чем больше ссылок, тем выше рейтинг страницы. Google также использует алгоритм расчета авторитетности PageRank, \nкоторый помогает ранжировать сайты в результатах поиска. В 2010 году компания запустила голосовой поиск в России. Чтобы воспользоваться им, нужно нажать на кнопку рядом со \nстрокой поиска на телефоне и произнести запрос. Ваш голос будет отправлен на сервер, браузер выдаст строку с распознанным запросом и результатами поиска.\nТекущий статус — активен",
                            reply_markup=next_keyboard)
    # if callback_query.data == 'button2':
    #     await bot.answer_callback_query(callback_query.id, text="СКОРО")


@dp.callback_query_handler(lambda c: c.data in ['Rambler'])
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    next_keyboard = types.InlineKeyboardMarkup()

    back1_button = types.InlineKeyboardButton("Назад", callback_data='Google')
    menu_button = types.InlineKeyboardButton("button1", callback_data='start')
    next_button = types.InlineKeyboardButton("Далее", callback_data='1.4')
    next_keyboard.add(back1_button, menu_button, next_button)

    new_photo_path = 'img/Rambler.png'  # Замените на имя вашего нового файла

    with open(new_photo_path, 'rb') as new_photo:
        await bot.send_photo(callback_query.from_user.id, 
                            photo=new_photo, 
                            caption="Rambler — одна из первых российских ИПС, открыта в 1996 году. В конце 2002 года была произведена коренная модернизация,\n после которой Rambler вновь вошел в группу лидеров сетевого поиска.\n В настоящее время объем индекса составляет порядка 150 миллионов документов. Для составления сложных запросов рекомендуется использовать режим\n “Детальный запрос”, который предоставляет широкие возможности для составления поискового предписания с помощью пунктов меню.\n Текущий статус — работает. \nПо результатам тестов Rambler занимает 2-ое место после Yandex. Производительность поискового робота декларируется в объеме 6,9 млн страниц в сутки. \nВ системе также усовершенствован поиск по новостям: робот посылается на ведущие новостные сайты России каждые 2 часа.",
                            reply_markup=next_keyboard)
    # if callback_query.data == 'button2':
    #     await bot.answer_callback_query(callback_query.id, text="СКОРО")




# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

