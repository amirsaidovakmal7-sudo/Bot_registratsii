import telebot
import buttons
import db

bot = telebot.TeleBot('8320858900:AAFRX0vARibmgkNKrPILbxVZ5A1IvoksfiE')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    if db.check(user_id):
        bot.send_message(user_id, f'Приветствую {username}. Хочешь узнаю твой возраст?'
                                  f'Введи свой год рождения',
                         reply_markup = telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, age)
    else:
        bot.send_message(user_id, 'Давай начнем регистрацию, напиши свое имя')
        bot.register_next_step_handler(message, getname)

def getname(message):
    user_id = message.from_user.id
    user_name = message.text
    if message.text.isalpha():
        bot.send_message(user_id, 'Теперь отправь свой номер',
                         reply_markup = buttons.button1())
        bot.register_next_step_handler(message, getnumber, user_name)
    else:
        bot.send_message(user_id, 'Имя неправильное, напиши коректно')
        bot.register_next_step_handler(message, getname)

def getnumber(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'Супер, теперь отправь локацию',
                         reply_markup = buttons.button2())
        bot.register_next_step_handler(message, getlocation, user_name, user_number)
    else:
        bot.send_message(user_id, 'Номер неверный, отправь коректный номер')
        bot.register_next_step_handler(message, getnumber, user_name)

def getlocation(message, user_name, user_number):
    user_id = message.from_user.id
    if message.location:
        user_location = message.location.latitude
        user_location2 = message.location.longitude
        db.register(user_id, user_name, user_number, user_location, user_location2)
        bot.send_message(user_id, 'Регистрация прошла успешно, данные сохранены. Теперь я дополнительно '
                                  'посчитаю твой возраст, введи свой год рождения',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, age)
    else:
        bot.send_message(user_id, 'Неверное сообщение, отправь локацию правильно')
        bot.register_next_step_handler(message, getlocation, user_name, user_number)


def age(message):
    user_id = message.from_user.id
    user_age = message.text
    year = 2025
    user_age1 = int(user_age)
    year-= user_age1
    bot.send_message(user_id, f'Тебе {year} лет')
    bot.send_message(user_id, 'В этом боте есть калькулятор, хочешь  попробовать?',
                     reply_markup = buttons.button3())
    bot.register_next_step_handler(message, calculator)

def calculator(message):
    user_id = message.from_user.id
    if message.text.lower() == 'нет':
        bot.send_message(user_id, 'Ну ладно(',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text.lower() == 'да':
        bot.send_message(user_id, 'Введи первое число',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, calculator2)

def calculator2(message):
    user_id = message.from_user.id
    user_num1 = message.text
    bot.send_message(user_id, 'Введи второе число')
    bot.register_next_step_handler(message, calculator3, user_num1)
def calculator3(message, user_num1):
    user_id = message.from_user.id
    user_num2 = message.text
    bot.send_message(user_id, 'Выбери операцию:'
                              '+, -, *(умножение), /(деление)')
    bot.register_next_step_handler(message, calculator4, user_num1, user_num2)
def calculator4(message, user_num1, user_num2):
    user_id = message.from_user.id
    user_operation = message.text
    if user_operation == '+':
        user_num3 = int(user_num1)
        user_num4 = int(user_num2)
        user_ans = user_num3 + user_num4
        bot.send_message(user_id, f'Результат = {user_ans}')
    elif user_operation == '-':
        user_num3 = int(user_num1)
        user_num4 = int(user_num2)
        user_ans = user_num3 - user_num4
        bot.send_message(user_id, f'Результат = {user_ans}')
    elif user_operation == '*':
        user_num3 = int(user_num1)
        user_num4 = int(user_num2)
        user_ans = user_num3 * user_num4
        bot.send_message(user_id, f'Результат = {user_ans}')
    elif user_operation == '/':
        user_num3 = int(user_num1)
        user_num4 = int(user_num2)
        user_ans = user_num3 / user_num4
        bot.send_message(user_id, f'Результат = {user_ans}')
    else:
        bot.send_message(user_id, 'Незнаю такой операции(')
        bot.register_next_step_handler(message, calculator)


bot.polling(none_stop=True)
