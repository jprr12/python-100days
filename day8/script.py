# functions with inputs; arguments and parameters
import math

# # Review: 
# # Create a function called greet(). 
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.
# def greet():
#     print("Hello.")
#     print("greet() is a sample function.")
#     print("Goodbye.")
# greet()

# # functions with input
# # def your_function(paramater):
# #   do this
# def my_function(name):
#     print(f"Hello {name}.")
#     print(f"Nice to meet you!")
# name = input("What's your name? ")
# my_function(name)

# # functions with 2 or more parameters
# def another_func(name, location):
#     print(f"Hello {name}! How's the weather in {location}?")
# name = input("What's your name: ")
# loc = input("Where do you live: ")
# another_func(name, loc)

# # coding exer day 8-1
# # painting area calculator w/ functions
# # 1 - create a function that calculates the number of cans needed to paint a wall area
# def paint_calc(height, width):
#     cans = (height * width)/5
#     round(cans)
#     print(f"You'll need {math.ceil(cans)} cans of paint.")
# # 2 - prompt user for height and width of wall
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# # 3 - call function
# paint_calc(height=test_h, width=test_w)

# # coding exer day 8-2
# # prime number checker
# # 1 - create a prime_checker function
# def prime_checker(number):
#     # initially check for single digit prime numbers
#     if ((number == 2) or (number == 3) or (number == 5) or (number == 7)):
#         print(f"{number} is a prime number.")
#     # check for none single digit prime numbers
#     elif ((number % 2 == 0) or (number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0)):
#         print(f"{number} is not a prime number.")
#     else:
#         print(f"{number} is a prime number.")
# n = int(input("Check this number: "))
# prime_checker(number=n)

