# control flow and logical operators

# # if/else
# print("Rollercoaster Ride!")
# height = int(input("Enter your height (cm): "))
# # condition
# if height > 120:
    # print("You can ride the rollercoaster. Hop in!")
# else: print("I'm sorry, but it's not safe for you to ride the rollercoaster.")

# # coding exer day3-1
# # odd or even
# # write a program that works out whether if a given number is an odd or even number
# # 1 - prompt user for an int
# num = int(input("enter a number: "))
# # 2 - check if num is even/ num%2 has no remainder
# if num%2 == 0:
    # print("This is an even number.")
# else: print("This is an odd number.")

# # nested if/elif
# print("Rollercoaster Ride!")
# height = int(input("Enter your height (cm): "))
# age = int(input("Enter your age: "))
# # condition
# if height > 120:
    # # nested if/else
    # if age < 12:
        # print("You can ride the rollercoaster for $5. Hop in!")
    # elif age >= 12 and age <= 18:
        # print("You can ride the rollercoaster for $7. Hop in!")
    # else: print("You can ride the rollercoaster for $12. Hop in!")
# else: print("I'm sorry, but it's not safe for you to ride the rollercoaster.")

# # coding exer day3-2
# # bmi 2.0
# # write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
# # 1 - prompt user for height & weight
# height = input("enter your height (m): ")
# weight = input("enter your weight (kg): ")
# # 2 - calculate bmi
# bmi = float(weight)/(float(height)**2)
# # 3 - set conditions
# if bmi < 18.5:
    # print(f"Your bmi is {round(bmi)}, you are underweight.")
# elif bmi > 18.5 and bmi < 25:
    # print(f"Your bmi is {round(bmi)}, you have a normal weight.")
# elif bmi > 25 and bmi < 30:
    # print(f"Your bmi is {round(bmi)}, you are slightly overweight.")
# elif bmi > 30 and bmi < 35:
    # print(f"Your bmi is {round(bmi)}, you are obese.")
# else: print(f"Your bmi is {round(bmi)}, you are clinically obese.")

# # coding exer day3-3
# # leap year (efficient version)
# # Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.
# # - leap years are divisible by 4 and 400, except by years divisible by 100
# # 1 - prompt user for year
# year = int(input("Which year do you want to check: "))
# # 2 - check if the year is divisible by 4 AND not divisible by 100 OR divisible by 400
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    # print(f"{year} is a leap year.")
# # run if all other conditions not satisfied
# else: print(f"{year} is not a leap year.")

# # rewriting leap year code - my version (clunky)
# year = int(input("input any year: "))
# if year % 4 == 0:
    # if year % 100 != 0 or year % 400 == 0:
        # print("leap year.")
    # else: print("not leap year.")
# else: print("not leap year.")

# # multiple if-statements in succession
# # roller coaster ride pt. 2
# print("Rollercoaster Ride 2!")
# height = int(input("Enter your height (cm): "))
# age = int(input("Enter your age: "))
# # set price of ride
# bill = 0
# # if condition satisfied, pay certain price
# if height > 120:
    # # nested if/else
    # if age < 12:
        # print("You can ride the rollercoaster for $5.")
        # bill = 5
    # elif age >= 12 and age <= 18:
        # print("You can ride the rollercoaster for $7.")
        # bill = 7
    # else: 
        # print("You can ride the rollercoaster for $12.")
        # bill = 12
    # # bill + 3 if they want photo
    # want_photo = input("Do you want a photo taken? Y/N: ")
    # if want_photo == 'y' or want_photo == "Y":
        # bill += 3
    # # total ride price
    # print(f"Your total bill for the ride is ${bill}.")
# # if condition not satisfied
# else: print("I'm sorry, but it's not safe for you to ride the rollercoaster.")

# # coding exer day 3-4
# # pizza order
# print("Welcome to Python Pizza Deliveries!")
# # 1 - prompt user for pizza size
# size = input("What size of pizza do you want? S, M, or L: ")
# # 2 - prompt user for pepperoni
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# # 3 - prompt user for extra cheese
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# # 4 - set pizza price to 0
# price = 0
# # 5 - set price based on size
# if size == 'S':
    # price += 15
# elif size == 'M':
    # price += 20
# elif size == 'L':
    # price += 25
# else: print("Invalid input.")
# # 6 - add price for pepperoni
# if add_pepperoni == 'Y':
    # if size == 'S':
        # price += 2
    # elif size == "M" or size == "L":
        # price += 3
    # else: print("Invalid input.")
# elif add_pepperoni == 'N':
    # price += 0
# else: print("Invalid input.")
# # 7 - add price for cheese
# if extra_cheese == 'Y':
    # price += 1
# elif extra_cheese == 'N':
    # price += 0
# else: print("Invalid input.")

# print(f"Your final bill is ${price}.")

# logical operators
# and, or, not

# # coding exer day3-5
# # name compatibility test
# print("Welcome to the Love Calculator!")
# # 1 - prompt user for 2 names
# name1 = input("Enter first name: ")
# name2 = input("Enter second name: ")
# # 2 - combine the 2 strings using concatenation; lowercase
# combName = name1.lower() + name2.lower()
# # 3 - count occurence of TRUE and LOVE in combName
# tCount = combName.count('t')
# rCount = combName.count('r')
# uCount = combName.count('u')
# eCount = combName.count('e')
# lCount = combName.count('l')
# oCount = combName.count('o')
# vCount = combName.count('v')
# # 4 - compute for love score
# loveScore = ((tCount + rCount + uCount + eCount) * 10) + (lCount + oCount + vCount + eCount)
# # 5 - score conditions
# compat = ""
# if loveScore < 10 or loveScore > 90:
    # compat = ", you go together like coke and mentos."
# elif loveScore > 40 and loveScore < 50:
    # compat = ", you are alright together."
# else: compat = "."
# # 6 - print result
# print(f"Your score is {loveScore}" + compat)

