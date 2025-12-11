from telebot import types
def button_language():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Рус')
    button2 = types.KeyboardButton('Eng')
    kb.add(button1, button2)
    return kb

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

def button4():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Send number', request_contact=True)
    kb.add(button1)
    return kb

def button5():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button2 = types.KeyboardButton('Send location', request_location=True)
    kb.add(button2)
    return kb

def button6():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = types.KeyboardButton('Yes')
    button4 = types.KeyboardButton('No')
    kb.add(button3)
    kb.add(button4)
    return kb
def button_stone_paper():
    kb = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
    button2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
    kb.add(button1, button2)
    return kb
def choose_thing():
    kb = types.InlineKeyboardMarkup(row_width=2)
    stone = types.InlineKeyboardButton(text='Камень', callback_data='stone')
    scissors = types.InlineKeyboardButton(text='Ножницы', callback_data='scissors')
    paper = types.InlineKeyboardButton(text='Бумага', callback_data='paper')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    kb.add(stone, scissors, paper, back)
    return kb

def button_stone_paper1():
    kb = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Yes', callback_data='yes1')
    button2 = types.InlineKeyboardButton(text='No', callback_data='no1')
    kb.add(button1, button2)
    return kb
def choose_thing1():
    kb = types.InlineKeyboardMarkup(row_width=2)
    stone = types.InlineKeyboardButton(text='Stone', callback_data='stone1')
    scissors = types.InlineKeyboardButton(text='Scissors', callback_data='scissors1')
    paper = types.InlineKeyboardButton(text='Paper', callback_data='paper1')
    back = types.InlineKeyboardButton(text='Back', callback_data='back1')
    kb.add(stone, scissors, paper, back)
    return kb

