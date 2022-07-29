from aiogram.dispatcher.filters.state import State, StatesGroup

class WhitelistFSM(StatesGroup):
    password = State()

class Select_car_FSM(StatesGroup):
    id = State()
    date = State()
    name_surname = State()
    d_or_n = State()

class ch_driver(StatesGroup):
    id = State()

class ch_driver_d(StatesGroup):
    id = State()
    y_n = State()
    id_del = State()