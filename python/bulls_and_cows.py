"""Import data from engine module"""
from bulls_and_cows_engine import get_number, check_number, is_end, ask_number


def start_game():
    """Method for staring game"""
    count = 0
    get_number()
    print('Компьютер загадал число')

    while True:
        user_input = ask_number()
        total_number = check_number(user_input)
        count += 1
        if is_end(total_number):
            print('Поздравляю, вы угадали число! Количество ходов:', count)
            print('Хотите еще партию? (Y/N)')
            if input() == 'Y':
                start_game()
            else:
                break


start_game()
