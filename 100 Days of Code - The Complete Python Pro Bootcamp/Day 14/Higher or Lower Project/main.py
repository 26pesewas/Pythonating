from game_data import data
from art import logo
from art import vs
import random


# selecting random numbers from data dictionary
first_dictionary = data[random.randint(0, 49)]
second_dictionary = data[random.randint(0, 49)]
if first_dictionary == second_dictionary:
    second_dictionary = data[random.randint(1, 51)]


def get_values(dictionary):
    """Returns a list of values obtained from a dictionary inputted"""
    name = dictionary['name']
    description = dictionary['description']
    country = dictionary['country']
    count = dictionary['follower_count']

    return name, description, country, count


def active_dictionary(user_guess):
    """Chooses which dictionary is the user's vs computer's based on user's response"""
    selected_dictionary = {}
    other_dictionary = {}

    # conditionals
    if user_guess == 'a':
        selected_dictionary = first_dictionary
        other_dictionary = second_dictionary
    elif user_guess == 'b':
        selected_dictionary = second_dictionary
        other_dictionary = first_dictionary

    return selected_dictionary, other_dictionary


def compare_score(first_score, second_score):
    """Compare scores based on user's selected dictionary to computer's dictionary"""
    if first_score > second_score:
        return "You got it right!"
    elif first_score < second_score:
        return "Wrong. Game over"


def game():
    """Play the higherlower game"""

    print(f"Compare A: {get_values(first_dictionary)[0]}, a {get_values(first_dictionary)[1]}, from {get_values(first_dictionary)[2]}.")
    print(vs)
    print(f"Against B: {get_values(second_dictionary)[0]}, a {get_values(second_dictionary)[1]}, from {get_values(second_dictionary)[2]}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # function to return user and computer's dictionary
    player_dictionary = active_dictionary(guess)[0]
    computer_dictionary = active_dictionary(guess)[1]

    # test
    print(player_dictionary)
    print(computer_dictionary)

    # obtaining follower count from player and computer dictionaries obtained based on user's guess
    player_score = get_values(player_dictionary)[3]
    computer_score = get_values(computer_dictionary)[3]

    # comparing score
    compare_score(player_score, computer_score)

continue_playing = False
while continue_playing:
    game()
    if first_response == "You got it right!":
        continue_playing = True
    else:






