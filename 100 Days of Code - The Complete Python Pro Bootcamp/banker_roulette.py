import random

# using random module to pick random person from the list
random_choice = random.randint(0, len(names) - 1)

print(f"{names[random_choice]} is going to buy the meal today!" )
