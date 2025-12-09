from telebot import types
def button1():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Отправить номер', request_contact=True)
    kb.add(button1)
    return kb

def button2():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button2 = types.KeyboardButton('Отправить локацию', request_location=True)
    kb.add(button2)
    return kb

def button3():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = types.KeyboardButton('Да')
    button4 = types.KeyboardButton('Нет')
    kb.add(button3)
    kb.add(button4)
    return kb

