from bulls_and_cows_engine import get_number, check_number, is_end, ask_number
from termcolor import cprint


def start_game():
    global count
    count = 0
    get_number()
    cprint('Компьютер загадал число', color='green')

    while True:
        user_input = ask_number()
        total_number = check_number(user_input)
        count += 1
        if is_end(total_number):
            print('Поздравляю, вы угадали число! Количество ходов:', count)
            cprint('Хотите еще партию? (Y/N)', color='yellow')
            if input() == 'Y':
                start_game()
            else:
                break


start_game()