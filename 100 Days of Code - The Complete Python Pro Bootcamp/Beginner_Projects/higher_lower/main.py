from game_data import data
from art import logo, vs
import random


def get_values(dictionary):
    """Returns a list of values obtained from a dictionary inputted"""
    name = dictionary['name']
    description = dictionary['description']
    country = dictionary['country']
    return f"{name}, a {description}, from {country} "


def compare_score(user_guess, first_score, second_score):
    """Checks which dictionary has the higher score and returns if user got it right"""
    if first_score > second_score:
        return user_guess == "a"
    else:
        return user_guess == "b"


# global variables
should_continue = True
score = 0
second_dictionary = random.choice(data)

while should_continue:
    # generating random dictionary from data dictionary
    first_dictionary = second_dictionary
    second_dictionary = random.choice(data)
    if first_dictionary == second_dictionary:
        second_dictionary = random.choice(data)

    """Play the higher lower game"""
    print(logo)
    print(f"Compare A: {get_values(first_dictionary)}")
    print(vs)
    print(f"Against B: {get_values(second_dictionary)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # clearing the screen
    print("\n" * 20)

    # obtain follower count from each dictionary
    first_count = first_dictionary["follower_count"]
    second_count = second_dictionary["follower_count"]

    # check if user is correct
    is_correct = compare_score(guess, first_count, second_count)

    # Give user feedback on their response
    if is_correct:
        score += 1
        print(f"You're right !. Your score is {score}")
    else:
        print(f"Oops. You got it wrong. Your final score is {score}")
        should_continue = False

