MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# global variable
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: Check if resources are sufficient when user orders a drink
def check_resources(selected_menu):
    """Check whether coffee machine has enough ingredients to make coffee chosen"""
    for ingredient in selected_menu:
        # loop through each item of what is in stock versus stock of coffee chosen
        if selected_menu[ingredient] < resources[ingredient]:
            print("We are green and go💚 ")
            return True
        else:
            print(f"Sorry, love. We are out of {ingredient} ")
            return False
    return True

#TODO: Process coins
def calculate_coins():
    """Takes in customer's coins and calculates its monetary value"""
    dimes = int(input("How many dimes ? ")) * 0.10
    quarters = int(input("How many quarters ? ")) * 0.25
    nickles = int(input("How many nickles ? ")) * 0.05
    pennies = int(input("How many pennies ? ")) * 0.01

    total_coins = "{:.2f}".format(dimes + quarters + nickles + pennies)

    return float(total_coins)

# TODO: Calculate change
def calculate_change(money, coffee_cost):
    """Process coins and calculate change"""
    if money < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif money > coffee_cost:
        amount_due  = round((money - coffee_cost),2)
        print(f"Here is ${amount_due} in change.")
        global profit
        profit += coffee_cost
        resources["money"] = f"${profit}"
        return True


# TODO: Reduce resources after order is processed
def reduce_stock(drink, coffee_dictionary):
    """Function that iterates along every item and deducts from resources after coffee is made"""
    for item in coffee_dictionary:
        resources[item] -= coffee_dictionary[item]

    print(f"Here is your {drink} ☕️. Enjoy!")


# TODO: Ask user what type of coffee they want
coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
coffee_ingredients = MENU[coffee_choice]["ingredients"]

# TODO: Print report based on user's choice
if coffee_choice == 'report':
    print(coffee_ingredients)

# TODO: Make coffee
if check_resources(coffee_ingredients):
    print("Please insert coins.")
    customer_money = calculate_coins()
    cost_of_coffee = MENU[coffee_choice]["cost"]

    # Checking if customer has enough to purchase coffee of choice
    if calculate_change(customer_money, cost_of_coffee):
        reduce_stock(coffee_choice,coffee_ingredients)
        print(resources)

more_coffee = True
while more_coffee:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == "off":
        print(resources)
        more_coffee = False
    elif coffee_choice == 'report':
        print(resources)
        more_coffee = False
    else:
        coffee_ingredients = MENU[coffee_choice]["ingredients"]
        if check_resources(coffee_ingredients):
            print("Please insert coins.")
            customer_money = calculate_coins()
            cost_of_coffee = MENU[coffee_choice]["cost"]
            # Checking if customer has enough to purchase coffee of choice
            if calculate_change(customer_money, cost_of_coffee):
                reduce_stock(coffee_choice, coffee_ingredients)
                print(resources)







