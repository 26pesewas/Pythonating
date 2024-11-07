from art import logo
import random


def no_of_attempts(difficulty):
    """function that returns number of  attempts"""
    attempts = 0
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5


def compare(u_number, c_number):
    """Compare user's guess to computer's number"""
    if u_number == c_number:
        return f"You got it! The answer was {c_number}"
    elif u_number < c_number:
        return "Too low."
    elif u_number > c_number:
        return "Too high."


def game():
    """Play the number-guessing game"""
    # generating a list from numbers 1 to 100
    numbers = []
    for i in range(1, 101):
        numbers.append(i)

    # select random number from the list numbers
    computer_number = random.choice(numbers)

    # start of game
    print(logo)
    print("I'm thinking of a number between 1 and 100")
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    number_of_attempts = no_of_attempts(game_level)
    print(computer_number)

    users_guess = int(input(f"You have {number_of_attempts} attempts remaining. Guess the number "))
    print(compare(users_guess, computer_number))

    # conditionals
    should_continue = False
    while not should_continue:
        comparison = compare(users_guess, computer_number)
        if comparison == f"You got it! The answer was {computer_number}":
            should_continue = True
        elif comparison == "Too low." or comparison == "Too high.":
            number_of_attempts -= 1
            if number_of_attempts == 1:
                users_guess = int(input(f"You have {number_of_attempts} attempt remaining. Guess the number "))
                print(compare(users_guess, computer_number))
            elif number_of_attempts == 0:
                should_continue = True
                print("You have no attempts remaining.")
            else:
                users_guess = int(input(f"You have {number_of_attempts} attempts remaining. Guess the number "))
                print(compare(users_guess, computer_number))


# function call
game()
