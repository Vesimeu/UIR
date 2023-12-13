import random
import tkinter as tk
from PIL import Image, ImageTk


def get_user_choice():
    user_choice = user_choice_var.get()
    return user_choice


def get_computer_choice():
    return random.randint(1, 3)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья"
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (
            user_choice == 3 and computer_choice == 1):
        return "Пользователь победил"
    else:
        return "Компьютер победил"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    user_image_label.config(image=image_dict[user_choice])
    computer_image_label.config(image=image_dict[computer_choice])

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result,font=("Arial", 16))


# Создаем окно
root = tk.Tk()
root.title("Игра 'Камень, ножницы, бумага'")

# Загружаем изображения
image_dict = {
    1: ImageTk.PhotoImage(Image.open("камень.png")),
    2: ImageTk.PhotoImage(Image.open("ножницы.png")),
    3: ImageTk.PhotoImage(Image.open("бумага.png")),
}

# Создаем интерфейс
user_choice_var = tk.IntVar()
user_choice_var.set(1)

frame = tk.Frame(root)
frame.pack(pady=10)

user_label = tk.Label(frame, text="Выберите:")
user_label.grid(row=0, column=0)

rock_radio = tk.Radiobutton(frame, text="Камень", variable=user_choice_var, value=1)
rock_radio.grid(row=1, column=0)

scissors_radio = tk.Radiobutton(frame, text="Ножницы", variable=user_choice_var, value=2)
scissors_radio.grid(row=1, column=1)

paper_radio = tk.Radiobutton(frame, text="Бумага", variable=user_choice_var, value=3)
paper_radio.grid(row=1, column=2)

play_button = tk.Button(frame, text="Играть", command=play_game)
play_button.grid(row=2, column=1)

user_image_label = tk.Label(root)
user_image_label.pack()

computer_image_label = tk.Label(root)
computer_image_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
