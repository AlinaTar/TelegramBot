from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from Project.handlers import states
from Project.keyboards import grafic_changes_kb, grafic_kb
from Project.keyboards import inline_select_car_kb, inline_del_ch_kb
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from Project.datebase import cars, changes


async def send_welcome(message: types.Message):
    await message.reply('Привет', reply_markup=grafic_changes_kb)


async def send_graphics(message: types.Message):
    selected_cars = cars.SelectTable('Xolyavskiy.db')
    for car in selected_cars:
        answer = f'id:{car[0]}\n{car[1]}'
        await message.reply(answer, reply_markup=inline_select_car_kb)
    await message.reply('Ок', reply_markup=grafic_kb)


async def select_car(callback: types.CallbackQuery):
    await states.Select_car_FSM.id.set()
    await callback.message.reply('Введите id выбранной машины')
    await callback.answer('')


async def select_car_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    await states.Select_car_FSM.next()
    await message.answer('Выберите дату', reply_markup=await SimpleCalendar().start_calendar())


async def select_car_date(callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)

    async with state.proxy() as data:
        if selected:
            data['date'] = date.strftime("%d/%m/%Y")
    await states.Select_car_FSM.next()
    await callback_query.message.reply('Введите своё Имя и Фамилию (напишите в одном сообщении)')


async def select_car_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sname'] = message.text
    await states.Select_car_FSM.next()
    await message.reply('Выберите день или ночь (напишите сообщением)')


async def select_car_dn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dn'] = message.text
        car = cars.selectFromids(data['id'], 'Xolyavskiy.db')
        date = data['date'] + " " + data['dn']
        changes.addNewchanges([car[0][1], data['sname'], date], 'Xolyavskiy.db')
    await state.finish()
    await message.reply('OK')


async def ch_car_id(message: types.Message):
    await states.ch_driver.id.set()
    cars_1 = cars.SelectTable('Xolyavskiy.db')
    for car in cars_1:
        await message.answer(f"id:{car[0]}\n {car[1]}")
    await message.answer("Введите id машины!")


async def ch_car_get(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id"] = message.text
        car = cars.selectFromids(data["id"], 'Xolyavskiy.db')
        ch = changes.selectFromnames(car[0][1], 'Xolyavskiy.db')
    for i in ch:
        await message.answer(f"{i[1]}\n ФИО: {i[2]}\n дата:{i[3]}")
    await state.finish()


async def ch_car_id_d(message: types.Message):
    await states.ch_driver_d.id.set()
    cars_1 = cars.SelectTable('Xolyavskiy.db')
    for car in cars_1:
        await message.answer(f"id:{car[0]}\n {car[1]}")
    await message.answer("Введите id машины!")


async def ch_car_get_d(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id"] = message.text
        car = cars.selectFromids(data["id"], 'Xolyavskiy.db')
        ch = changes.selectFromnames(car[0][1], 'Xolyavskiy.db')
    for i in ch:
        await message.answer(f"id:{i[0]}\n{i[1]}\n ФИО: {i[2]}\n дата:{i[3]}")
    await message.reply("Хотите ли вы удалить кого-то со смены?(Напишите одним сообщением: Да или Нет)")
    await states.ch_driver_d.next()

async def del_ch(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await message.reply("Выберите id смены которую хотите удалить")
        await states.ch_driver_d.next()
    else:
        await message.reply("Ok")
        await state.finish()

async def del_ch_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id"]= message.text
        changes.deleteRecord(data["id"], 'Xolyavskiy.db')
    await message.reply("Ok")
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'], state=None)
    dp.register_message_handler(send_graphics, Text(equals='График', ignore_case=True), state=None)
    dp.register_callback_query_handler(select_car, text='select car', state=None)
    dp.register_message_handler(select_car_id, state=states.Select_car_FSM.id)
    dp.register_callback_query_handler(select_car_date, simple_cal_callback.filter(), state=states.Select_car_FSM.date)
    dp.register_message_handler(select_car_name, state=states.Select_car_FSM.name_surname)
    dp.register_message_handler(select_car_dn, state=states.Select_car_FSM.d_or_n)
    dp.register_message_handler(ch_car_id, Text(equals="График для водителя", ignore_case=True), state=None)
    dp.register_message_handler(ch_car_get, state=states.ch_driver.id)
    dp.register_message_handler(ch_car_id_d,Text(equals="График для руководителя", ignore_case=True), state=None)
    dp.register_message_handler(ch_car_get_d, state=states.ch_driver_d.id)
    dp.register_message_handler(del_ch,state=states.ch_driver_d.y_n)
    dp.register_message_handler(del_ch,state=states.ch_driver_d.id_del)