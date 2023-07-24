# day 16 project - recreating coffee machine project using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects for each class
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    # gets the available items on the menu
    options = menu.get_items()
    # ask user what coffee they're buying
    choice = input(f"What would you like? ({options}report/off): ").lower()
    # turns the machine off/terminates program
    if choice == 'off':
        print("Coffee machine is now turned off.")
        machine_on = False
    # prints current coffee machine resource status
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        # finds user input in the menu and returns all its attributes (name, water, milk, etc.)
        drink = menu.find_drink(choice)
        # checks if user typed the right drink
        if drink == 0:
            continue
        else:
            # check if machine resource and user payment are sufficient
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                # make the coffee
                coffee_maker.make_coffee(drink)

