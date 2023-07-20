# debugging, fixing errors

# debugging 
# - process of finding and removing bugs in your code

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# # bug: for loop doesn't really get to 20 since range func isn't inclusive of the 2nd parameter
# # fix: change the range's 2nd parameter to anything > 20, or change i == 1-19

# ==============================================
# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# # bug: dice_imgs[] only has index ranging from 0-5. if dice_num hits 6, that will produce an error
# # fix: print(dice_imgs[dice_num-1]) or dice_num = randint(0, 5)

# ==============================================
# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# # bug: if year == 1994, nothing happens because 1994 is excluded in both conditions
# # fix: either = in first or second 1994 condition

# ==============================================
# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# # bug: print statement isn't indented, age isn't an integer and can't be compared to another int, print statement isn't an f-string, therefore {age} can't be displayed
# # fix: age = int(input("...")), [tab]print(f"...{age}")

# ==============================================
# # using print statements as a debugger
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # bug: words_per_page is using equality operator instead of assignment operator
# # fix: change the equality operator to =

# ==============================================
# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)
# mutate([1,2,3,5,8,13])
# # intended: mutate() prints 6 items on the list with their values doubled
# # actual: mutate() only prints 1 item on the list
# # bug: b_list.append() is called outside the for-loop instead of inside
# # fix: indent b_list.append() to put it inside the loop

# ==============================================
# # coding exer day 13-1 - debugging odd/even exer
# num = int(input("Enter a number: "))
# if num % 2 = 0:
#     print("This is an even number.")
# else: 
#     print("This is an odd number.")
# # bug: if statement uses assignment instead of comparison operator
# # fix: change to ==

# ==============================================
# # coding exer day 13-2 - debugging leap year exer
# year = input("Which year do you want to check?")
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
# # bug - year is not converted into an int
# # fix - convert year to int

# ==============================================
# coding exer day 13-3 - debgging fizz buzz exer
for num in range(1, 101):
    # if num % 3 == 0 or num % 5 == 0:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    if num % 3 == 0:
        print("Fizz")
    # if num % 5 == 0:
    elif num % 5 == 0:
        print("Buzz")
    else:
        # print([num])
        print(num)
# bug: 1 - code is printing a list item instead of the actual item, 2 - if statement is misused
# fix - replace elif to the succeeding if statements, print(num) instead, replace or -> and

