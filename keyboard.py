 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Объяевление кнопок и их название
button1 = KeyboardButton("анекдот")
markup1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1)
