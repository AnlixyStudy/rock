import random

def get_user_choice():
    user_input = input("Выберите камень, ножницы или бумагу: ")
    choices = {'камень': 1, 'ножницы': 2, 'бумага': 3}
    
    while user_input.lower() not in choices:
        print("Неверный выбор. Попробуйте еще раз.")
        user_input = input("Выберите камень, ножницы или бумагу: ")

    return choices[user_input.lower()]

def get_computer_choice():
    return random.choice(list(choices.keys()))

def determine_winner(user_choice, computer_choice):
    print(f"Компьютер выбрал: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 1 and computer_choice == 'ножницы') or \
         (user_choice == 2 and computer_choice == 'бумага') or \
         (user_choice == 3 and computer_choice == 'камень'):
        print("Поздравляю, вы победили!")
    else:
        print(f"Вы проиграли! Компьютер выбрал: {choices[computer_choice]}")

choices = {'камень': 1, 'ножницы': 2, 'бумага': 3}

user_choice = get_user_choice()
computer_choice = get_computer_choice()

determine_winner(user_choice, computer_choice)
