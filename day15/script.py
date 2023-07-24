# local development environment
# coffee magechine code project

from data import coffee_data

def eval(coffee):
    '''
    - calculates the the price of coffee
    - returns false if user is short on money; returns true otherwise
    '''
    # loops through the coffee list to find the price of coffee
    for i in range(len(coffee_data)):
        if coffee_data[i]['type'].lower() == coffee:            
            coffee_price = coffee_data[i]['price']
            print(f"{coffee.title()} costs ${coffee_price}")
    # asks user for coins, calculates total coins
    print("Please insert coins.")
    user_coins = int(input("Insert quarters: ")) * 0.25
    user_coins += int(input("Insert dimes: ")) * 0.10
    user_coins += int(input("Insert nickels: ")) * 0.05
    user_coins += int(input("Insert pennies: ")) * 0.01
    print(f"Your coin total is ${user_coins}.")
    # refunds if short
    if user_coins < coffee_price:
        print(f"You are ${round((coffee_price - user_coins), 2)} short. Money refunded.")
        return False
    else:
        print(f"Here is ${round((user_coins - coffee_price), 2)} in change.")
        print(f"Enjoy your {coffee}!")
        return True

def machine_in_operation():
    '''start of coffee machine'''
    # initializes coffee machine resources
    current_water = 300
    current_milk = 200
    current_coffee = 100
    current_money = 0
    # start of loop
    machine_on = True
    while machine_on:
        # ask user what they like to do with the machine
        choice = input("What would you like? (espresso/latte/cappuccino/report/refill/off): ").lower()
        # turns the machine off
        if choice == 'off':
            print("Coffee machine is now off.")
            machine_on = False
        # prints the current machine resources
        elif choice == 'report':
            print("Current machine status")
            print(f"Water: {current_water} ml\nMilk: {current_milk} ml\nCoffee: {current_coffee} ml\nMoney: ${current_money}")
        # loops through the coffee list to get the necessary resources from the machine
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            for i in range(len(coffee_data)):
                if coffee_data[i]['type'].lower() == choice:
                    # checks first if the machine has enough resources
                    # NOTE: this could be further optimized by changing the current machine resource to a list similar to the coffee data list
                    if (coffee_data[i]['water'] > current_water) or (coffee_data[i]['milk'] > current_milk) or (coffee_data[i]['coffee'] > current_coffee):
                        print("Sorry, not enough resource in the machine.")
                    else:
                        # if machine has enough resource but user don't have enough money
                        # refund
                        if not eval(choice):
                            break
                        # if conditions are satisfied, resources will be deducted from machine to make coffee, and then add money
                        else:
                            current_water -= coffee_data[i]['water']
                            current_milk -= coffee_data[i]['milk']
                            current_coffee -= coffee_data[i]['coffee']
                            current_money += coffee_data[i]['price']
        # refills the coffee machine resources
        elif choice == 'refill':
            current_water = 300
            current_milk = 200
            current_coffee = 100
            print("Machine is now refilled!")
        else:
            print("Wrong command.")


machine_in_operation()

