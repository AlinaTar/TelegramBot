from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

grafic_button = KeyboardButton('График')
changes_button = KeyboardButton('Отчёт по сменам')
grafic_changes_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
grafic_changes_kb.row(grafic_button,changes_button)

grafic_for_driver = KeyboardButton('График для водителя')
grafic_for_director = KeyboardButton('График для руководителя')

grafic_kb = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
grafic_kb.row(grafic_for_director,grafic_for_driver)
