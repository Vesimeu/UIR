import random
import tkinter as tk
from PIL import Image, ImageTk

def get_user_choice():
    while True:
        user_choice = input("Выберите: камень (1), ножницы (2), бумагу (3): ")
        if user_choice in ["1", "2", "3"]:
            return int(user_choice)
        else:
            print("Пожалуйста, выберите 1, 2 или 3.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья"
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        return "Пользователь победил"
    else:
        return "Компьютер победил"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    local_name = return_word(user_choice)
    print(f"Пользователь выбрал {user_choice} - {local_name}")
    local_name = return_word(computer_choice)
    print(f"Компьютер выбрал {computer_choice} - {local_name}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
def return_word(A):
    if (A == 1):
        return "камень ()"
    if (A==2):
        return "ножницы \/"
    if (A==3):
        return "бумага #"


def main():
    print("Игра 'Камень, ножницы, бумага'")
    while True:
        level = int(input("Выберите уровень игры (1, 2 или 3):  "))
        if level == 1:
            play_game()
        elif level == 2:
            play_game()
            play_again = input("Хотите сыграть ещё раз? (да/нет): ")
            if play_again.lower() != "да":
                break
        elif level == 3:
            rounds = int(input("Введите количество раундов: "))
            user_score = 0
            computer_score = 0
            for _ in range(rounds):
                user_choice = get_user_choice()
                computer_choice = get_computer_choice()
                print(f"Пользователь выбрал {user_choice} - {return_word(user_choice)}")
                print(f"Компьютер выбрал {computer_choice} - {return_word(user_choice)}")
                result = determine_winner(user_choice, computer_choice)
                if result == "Пользователь победил":
                    user_score += 1
                elif result == "Компьютер победил":
                    computer_score += 1
            if user_score > computer_score:
                print(f"Поздравляю, Вы победили со счетом {user_score}:{computer_score}")
            elif user_score < computer_score:
                print(f"Компьютер победил со счетом {computer_score}:{user_score}")
            else:
                print(f"Итог турнира: Ничья ({user_score}:{computer_score})")
            play_again = input("Хотите сыграть ещё раз? (да/нет): ")
            if play_again.lower() != "да" or play_again.lower() != "Да":
                break
        else:
            print("Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
