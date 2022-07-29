from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_select_car_button = InlineKeyboardButton('Выбрать машину', callback_data='select car')
inline_select_car_kb = InlineKeyboardMarkup()
inline_select_car_kb.add(inline_select_car_button)

inline_del_ch_button = InlineKeyboardButton('Удалить смену', callback_data='del ch')
inline_del_ch_kb = InlineKeyboardMarkup()
inline_del_ch_kb.add(inline_del_ch_button)