"""Installing random package"""
import random

MAX_NUMBER = 4
number_list = []


def get_number():
    """Get random number"""
    number_list.append(random.randint(1, 9))
    while len(number_list) < MAX_NUMBER:
        random_int = random.randint(0, 9)
        if random_int not in number_list:
            number_list.append(random_int)


def ask_number():
    """Asking a number from user"""
    while True:
        print('Введите четырехзначное число')
        user_input = input()
        set_user_input = set(user_input)
        if user_input.isdigit() is False:
            print('Вы ввели не число')
        elif len(set_user_input) != len(user_input):
            print('Вы ввели число с повторяющимися цифрами')
        elif str(user_input)[0] == '0':
            print('Вы ввели число, начинающееся на ноль')
        elif len(user_input) != MAX_NUMBER:
            print('Вы ввели не четырехзначное число')
        else:
            return user_input


def check_number(user_input):
    """Checking two numbers"""
    user_number = list(str(user_input))
    total_number = {'bulls': 0, 'cows': 0}
    for i, number in enumerate(user_number):
        if int(number) in number_list:
            if int(number) == number_list[i]:
                total_number['bulls'] += 1
            else:
                total_number['cows'] += 1
    print('Быков:', total_number['bulls'], ', коров:', total_number['cows'])
    return total_number


def is_end(total_number):
    """function for the end of game"""
    return total_number['bulls'] == MAX_NUMBER
