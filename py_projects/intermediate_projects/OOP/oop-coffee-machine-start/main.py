from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# creating objectS from classes
my_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on  = True



while is_on:
    drink_options = menu.get_items()
    choice = input(f"What would you like to order? {drink_options} ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_machine.report()
        coffee_maker.report()
    else:
        # finding drink
        drink = menu.find_drink(choice)

        # check if resources are sufficient and process coins
        if coffee_maker.is_resource_sufficient(drink) and my_machine.make_payment(drink.cost):
            # make coffee
            coffee_maker.make_coffee(drink)
        else:
            is_on = False