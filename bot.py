import telebot
import buttons
import db
import random

bot = telebot.TeleBot('8320858900:AAECrQIgVPbZE6dJXsOj4g8922e2kg2jgbQ')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Выбери язык',
                     reply_markup=buttons.button_language())
@bot.message_handler(func=lambda m: m.text in ['Рус', 'Eng'])
def full_language_programm(message):
    user_id = message.from_user.id
    user_language = message.text
    if user_language == 'Рус':
        username = message.from_user.username
        if db.check(user_id):
            bot.send_message(user_id, f'Приветствую {username}. Хочешь узнаю твой возраст? '
                                      f'Введи свой год рождения',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, age, user_language)
        else:
            bot.send_message(user_id, 'Давай начнем регистрацию, напиши свое имя',
                             reply_markup=telebot.types.ReplyKeyboardRemove())

            bot.register_next_step_handler(message, getname, user_language)
    elif user_language == 'Eng':
        if db.check(user_id):
            username = message.from_user.username
            bot.send_message(user_id, f'Hello {username}. Do you want me to know your age? '
                                      f'Enter your year of birth',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, age, user_language)
        else:
            bot.send_message(user_id, 'Let start the regestration, enter your name',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, getname, user_language)
    else:
        bot.send_message(user_id, 'Язык выбран неверно. Выбери по кнопке')
        bot.send_message(user_id, 'Language was choosen incorrectly. Choose by button',
                         reply_markup=buttons.button_language())
        bot.register_next_step_handler(message, full_language_programm)





def getname(message, user_language):
    user_id = message.from_user.id
    if user_language == 'Рус':
        user_name = message.text
        if message.text.isalpha():
            bot.send_message(user_id, 'Теперь отправь свой номер',
                             reply_markup=buttons.button1())
            bot.register_next_step_handler(message, getnumber, user_name, user_language)
        else:
            bot.send_message(user_id, 'Имя неправильное, напиши коректно')
            bot.register_next_step_handler(message, getname, user_language)
    elif user_language == 'Eng':
        user_name = message.text
        if message.text.isalpha():
            bot.send_message(user_id, 'Then send your number',
                             reply_markup=buttons.button4())
            bot.register_next_step_handler(message, getnumber, user_name, user_language)
        else:
            bot.send_message(user_id, 'Name is incorrect, write correctly')
            bot.register_next_step_handler(message, getname, user_language)

def getnumber(message, user_name, user_language):
    user_id = message.from_user.id
    if user_language == 'Рус':
        if message.contact:
            user_number = message.contact.phone_number
            bot.send_message(user_id, 'Супер, теперь отправь локацию',
                             reply_markup=buttons.button2())
            bot.register_next_step_handler(message, getlocation, user_name, user_number, user_language)
        else:
            bot.send_message(user_id, 'Номер неверный, отправь коректный номер')
            bot.register_next_step_handler(message, getnumber, user_name, user_language)
    elif user_language == 'Eng':
        if message.contact:
            user_number = message.contact.phone_number
            bot.send_message(user_id, 'Great! Then, send your location',
                             reply_markup=buttons.button5())
            bot.register_next_step_handler(message, getlocation, user_name, user_number, user_language)
        else:
            bot.send_message(user_id, 'Number is incorrect, send it by button')
            bot.register_next_step_handler(message, getnumber, user_name, user_language)

def getlocation(message, user_name, user_number, user_language):
    user_id = message.from_user.id
    if user_language == 'Рус':
        if message.location:
            user_location = message.location.latitude
            user_location2 = message.location.longitude
            db.register(user_id, user_name, user_number, user_location, user_location2)
            bot.send_message(user_id, 'Регистрация прошла успешно, данные сохранены. Теперь я дополнительно '
                                      'посчитаю твой возраст, введи свой год рождения',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, age, user_language)
        else:
            bot.send_message(user_id, 'Неверное сообщение, отправь локацию правильно')
            bot.register_next_step_handler(message, getlocation, user_name, user_number, user_language)
    elif user_language == 'Eng':
        if message.location:
            user_location = message.location.latitude
            user_location2 = message.location.longitude
            db.register(user_id, user_name, user_number, user_location, user_location2)
            bot.send_message(user_id, 'Registration was successful, data saved. Now I will additionally calculate '
                                      'your age, enter your year of birth',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, age, user_language)
        else:
            bot.send_message(user_id, 'Incorrect message, send your location correctly')
            bot.register_next_step_handler(message, getlocation, user_name, user_number, user_language)



def age(message, user_language):
    try:
        user_id = message.from_user.id
        user_age = message.text
        year = 2025
        user_age1 = int(user_age)
        year -= user_age1
        if user_language == 'Рус':
            bot.send_message(user_id, f'Твой возраст: {year} лет')
            bot.send_message(user_id, 'В этом боте есть калькулятор, хочешь  попробовать?',
                             reply_markup=buttons.button3())
            bot.register_next_step_handler(message, calculator, user_language)
        elif user_language == 'Eng':
            bot.send_message(user_id, f'Your age: {year} years old')
            bot.send_message(user_id, 'This bot hs a calculator, do you wana try?',
                             reply_markup=buttons.button6())
            bot.register_next_step_handler(message, calculator, user_language)
    except ValueError:
        if user_language == 'Рус':
            bot.send_message(message.from_user.id, 'Что-то пошло не так. Введи свой год рождения корректно')
            bot.register_next_step_handler(message, age, user_language)
        elif user_language == 'Eng':
            bot.send_message(message.from_user.id, 'Something went wrong. Write your date of birth correctly')
            bot.register_next_step_handler(message, age, user_language)


def calculator(message, user_language):
    user_id = message.from_user.id
    if user_language == 'Рус':
        if message.text.lower() == 'нет':
            bot.send_message(user_id, 'Ну ладно(',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.send_message(user_id, 'А еще в боте есть игра камень ножницы '
                                      'бумага. хочешь попробовать?',
                             reply_markup=buttons.button_stone_paper())
        elif message.text.lower() == 'да':
            bot.send_message(user_id, 'Введи первое число',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, calculator2, user_language)
        else:
            bot.send_message(user_id, 'Неверный ответ, отправь по кнопке',
                             reply_markup=buttons.button3())
            bot.register_next_step_handler(message, calculator, user_language)
    elif user_language == 'Eng':
        if message.text.lower() == 'no':
            bot.send_message(user_id, 'Okay(',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.send_message(user_id, 'The bot also has a game called "stone, paper, scissors." '
                                      'Want to try it?',
                             reply_markup=buttons.button_stone_paper1())
        elif message.text.lower() == 'yes':
            bot.send_message(user_id, 'Enter first number',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, calculator2, user_language)
        else:
            bot.send_message(user_id, 'Wrong answer. Choose "yes" or "no"',
                             reply_markup=buttons.button6())
            bot.register_next_step_handler(message, calculator, user_language)


def calculator2(message, user_language):
    user_id = message.from_user.id
    user_num1 = message.text
    if user_language == 'Рус':
        bot.send_message(user_id, 'Введи второе число')
        bot.register_next_step_handler(message, calculator3, user_num1, user_language)
    elif user_language == 'Eng':
        bot.send_message(user_id, 'Enter second number')
        bot.register_next_step_handler(message, calculator3, user_num1, user_language)
def calculator3(message, user_num1, user_language):
    user_id = message.from_user.id
    user_num2 = message.text
    if user_language == 'Рус':
        bot.send_message(user_id, 'Выбери операцию: ',
                         reply_markup=buttons.calculator_operation())
        bot.register_next_step_handler(message, calculator4, user_num1, user_num2, user_language)
    elif user_language == 'Eng':
        bot.send_message(user_id, 'Choose operation: ',
                         reply_markup=buttons.calculator_operation1())
        bot.register_next_step_handler(message, calculator4, user_num1, user_num2, user_language)

def calculator4(message, user_num1, user_num2, user_language):
    user_id = message.from_user.id
    user_operation = message.text
    try:
        if user_operation == '+':
            user_num3 = int(user_num1)
            user_num4 = int(user_num2)
            user_ans = user_num3 + user_num4
            if user_language == 'Рус':
                bot.send_message(user_id, f'Результат = {user_ans}',
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                bot.send_message(user_id, 'А еще в боте есть игра '
                                          f'камень ножницы бумага, хочешь попробовать?',
                                 reply_markup=buttons.button_stone_paper())
            elif user_language == 'Eng':
                bot.send_message(user_id, f'Answer = {user_ans}',
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                bot.send_message(user_id, 'The bot also has a game called "stone, paper, scissors."'
                                          f' Want to try it?',
                                 reply_markup=buttons.button_stone_paper1())
        elif user_operation == '-':
            user_num3 = int(user_num1)
            user_num4 = int(user_num2)
            user_ans = user_num3 - user_num4
            if user_language == 'Рус':
                bot.send_message(user_id, f'Результат = {user_ans}',
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                bot.send_message(user_id, 'А еще в боте есть игра '
                                          f'камень ножницы бумага, хочешь попробовать?',
                                 reply_markup=buttons.button_stone_paper())
            elif user_language == 'Eng':
                bot.send_message(user_id, f'Answer = {user_ans}',
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                bot.send_message(user_id, 'The bot also has a game called "stone, paper, scissors."'
                                          f' Want to try it?',
                                 reply_markup=buttons.button_stone_paper1())
        elif user_operation == '*':
            user_num3 = int(user_num1)
            user_num4 = int(user_num2)
            user_ans = user_num3 * user_num4
            if user_language == 'Рус':
                bot.send_message(user_id, f'Результат = {user_ans}',
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                bot.send_message(user_id, 'А еще в боте есть игра '
                                          f'камень ножницы бумага, хочешь попробовать?',
                                 reply_markup=buttons.button_stone_paper())
            elif user_language == 'Eng':
                bot.send_message(user_id, f'Answer = {user_ans}',
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                bot.send_message(user_id, 'The bot also has a game called "stone, paper, scissors."'
                                          f' Want to try it?',
                                 reply_markup=buttons.button_stone_paper1())
        elif user_operation == ':':
            user_num3 = int(user_num1)
            user_num4 = int(user_num2)
            user_ans = user_num3 / user_num4
            if user_language == 'Рус':
                bot.send_message(user_id, f'Результат = {user_ans}',
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                bot.send_message(user_id, 'А еще в боте есть игра '
                                          f'камень ножницы бумага, хочешь попробовать?',
                                 reply_markup=buttons.button_stone_paper())

            elif user_language == 'Eng':
                bot.send_message(user_id, f'Answer = {user_ans}',
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                bot.send_message(user_id, 'The bot also has a game called "stone, paper, scissors."'
                                          f' Want to try it?',
                                 reply_markup=buttons.button_stone_paper1())
        else:
            if user_language == 'Рус':
                bot.send_message(user_id, 'Не знаю такой операции, выбери по кнопке')
                bot.register_next_step_handler(message, calculator4, user_num1, user_num2, user_language)
            elif user_language == 'Eng':
                bot.send_message(user_id, 'I dont know this operation(Choose by button')
                bot.register_next_step_handler(message, calculator4, user_num1, user_num2, user_language)
    except Exception:
        if user_language == 'Рус':
            bot.send_message(user_id, 'Что-то пошло не так. '
                                      'Введи первое и второе число правильно',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, calculator2, user_language)
        elif user_language == 'Eng':
            bot.send_message(user_id, 'Something went wrong. '
                                      'Enter first and second number correctly',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, calculator2, user_language)

@bot.callback_query_handler(lambda call: call.data in ['yes', 'no'])
def game(call):
    values = call.data
    user_id = call.message.chat.id
    if values == 'no':
        bot.delete_message(chat_id=user_id, message_id=call.message.message_id)
        bot.send_message(user_id, 'Хорошо(')
    elif values == 'yes':
       bot.send_message(user_id, 'Выбери предмет',
                        reply_markup=buttons.choose_thing())
    else:
        bot.send_message(user_id, 'Неверный ответ, выбери да или нет по кнопке',
                         reply_markup=buttons.button_stone_paper())
        bot.register_next_step_handler(call, game)


@bot.callback_query_handler(lambda call: call.data in ['stone', 'scissors', 'paper', 'back'])
def choice(call):
    user_id = call.message.chat.id
    words = ['Камень', 'Ножницы', 'Бумага']
    random_word = random.choice(words)

    if call.data == 'stone' and random_word == 'Камень':
        bot.send_message(user_id, f'Я выбрал Камень, ничья! '
                                     f'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())

    elif call.data == 'stone' and random_word == 'Ножницы':
        bot.send_message(user_id, 'Я выбрал Ножницы, ты победил! '
                                     'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())
    elif call.data == 'stone' and random_word == 'Бумага':
        bot.send_message(user_id, 'Я выбрал Бумагу, я победил! '
                                     'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())

    elif call.data == 'scissors' and random_word == 'Камень':
        bot.send_message(user_id, f'Я выбрал Камень, я победил! '
                                     f'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())
    elif call.data == 'scissors' and random_word == 'Ножницы':
        bot.send_message(user_id, 'Я выбрал Ножницы, ничья! '
                                     'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())
    elif call.data == 'scissors' and random_word == 'Бумага':
        bot.send_message(user_id, 'Я выбрал Бумагу, ты победил! '
                                     'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())

    elif call.data == 'paper' and random_word == 'Камень':
        bot.send_message(user_id, f'Я выбрал Камень, ты победил! '
                                     f'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())
    elif call.data == 'paper' and random_word == 'Ножницы':
        bot.send_message(user_id, 'Я выбрал Ножницы, я победил! '
                                     'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())
    elif call.data == 'paper' and random_word == 'Бумага':
        bot.send_message(user_id, 'Я выбрал Бумагу, ничья! '
                                     'Если хочешь еще, выбери предмет заново',
                        reply_markup=buttons.choose_thing())

    elif call.data == 'back':
        bot.send_message(user_id, 'Игра окончена!',
                        reply_markup=telebot.types.ReplyKeyboardRemove())

    else:
        bot.send_message(user_id, 'Что то пошло не так, нажми по кнпоке',
                        reply_markup=buttons.choose_thing())



@bot.callback_query_handler(lambda call: call.data in ['yes1', 'no1'])
def game1(call):
    values = call.data
    user_id = call.message.chat.id
    if values == 'no1':
        bot.send_message(user_id, 'Okay(')
    elif values == 'yes1':
       bot.send_message(user_id, 'Choose item',
                        reply_markup=buttons.choose_thing1())
    else:
        bot.send_message(user_id, 'Something went wrong. Choose "yes" or "no"',
                         reply_markup=buttons.button_stone_paper())
        bot.register_next_step_handler(call, game1)


@bot.callback_query_handler(lambda call: call.data in ['stone1', 'scissors1', 'paper1', 'back1'])
def choice1(call):
    user_id = call.message.chat.id
    words1 = ['Stone', 'Scissors', 'Paper']
    random_word1 = random.choice(words1)

    if call.data == 'stone1' and random_word1 == 'Stone':
        bot.send_message(user_id, f'I choosed Stone, dwaw! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())

    elif call.data == 'stone1' and random_word1 == 'Scissors':
        bot.send_message(user_id, f'I choosed Scissors, you win! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())
    elif call.data == 'stone1' and random_word1 == 'Paper':
        bot.send_message(user_id, f'I choosed Paper, I win! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())

    elif call.data == 'scissors1' and random_word1 == 'Stone':
        bot.send_message(user_id, f'I choosed scissors, you win! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())
    elif call.data == 'scissors1' and random_word1 == 'Scissors':
        bot.send_message(user_id, f'I choosed scissors, draw! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())
    elif call.data == 'scissors1' and random_word1 == 'Paper':
        bot.send_message(user_id, f'I choosed Paper, you win! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())

    elif call.data == 'paper1' and random_word1 == 'Stone':
        bot.send_message(user_id, f'I choosed Stone, you win! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())
    elif call.data == 'paper1' and random_word1 == 'Scissors':
        bot.send_message(user_id, f'I choosed Scissors, I win! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())
    elif call.data == 'paper1' and random_word1 == 'Paper':
        bot.send_message(user_id, f'I choosed Paper, draw! '
                                     f'If you want play again, choose item again',
                        reply_markup=buttons.choose_thing1())

    elif call.data == 'back1':
        bot.send_message(user_id, 'Game finished!',
                        reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'Something went  wrong, click the button',
                        reply_markup=buttons.choose_thing1())



bot.polling(none_stop=True)