import random
from termcolor import cprint

MAX_NUMBER = 4


def get_number():
    global number_list
    number_list = []
    number_list.append(random.randint(1, 9))
    while len(number_list) < MAX_NUMBER:
        x = random.randint(0, 9)
        if x not in number_list:
            number_list.append(x)


def ask_number():
    while True:
        cprint('Введите четырехзначное число', color='white')
        user_input = input()
        set_user_input = set(user_input)
        if user_input.isdigit() is False:
            cprint('Вы ввели не число', color='red')
        elif len(set_user_input) != len(user_input):
            cprint('Вы ввели число с повторяющимися цифрами', color='red')
        elif str(user_input)[0] == '0':
            cprint('Вы ввели число, начинающееся на ноль', color='red')
        elif len(user_input) != MAX_NUMBER:
            cprint('Вы ввели не четырехзначное число', color='red')
        else:
            return user_input


def check_number(user_input):
    user_number = list(str(user_input))
    total_number = {'bulls': 0, 'cows': 0}
    for i, y in enumerate(user_number):
        if int(y) in number_list:
            if int(user_number[i]) == number_list[i]:
                total_number['bulls'] += 1
            else:
                total_number['cows'] += 1
    print('Быков:', total_number['bulls'], ', коров:', total_number['cows'])
    return total_number


def is_end(total_number):
    return total_number['bulls'] == MAX_NUMBER
