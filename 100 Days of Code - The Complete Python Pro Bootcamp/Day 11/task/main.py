import random
from art import logo

def deal_card():
    """Returns a random choice from the cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card


def calculate_score(cards):
    """Takes a list as input and returns the sum of the items in the list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Computer has blackjack! You lose! 🤣"
    elif u_score == 0:
        return "Blackjack! You win! 🤩"
    elif u_score > 21:
        return "You went over. You lose 🤣"
    elif c_score > 21:
        return "Computer went over. You win 🤩"
    elif u_score > c_score:
        return "You win 🤩"
    else:
        return "You lose 🤣"


def play_game():
    """Plays the blackjack game"""
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # user-side functionalities
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your deck: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_game = input("Do you want to deal? Type 'y' for yes or 'n' to pass ")
            if continue_game == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type y or n. ") == 'y':
    print("\n" * 10)
    play_game()