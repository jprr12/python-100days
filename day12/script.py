# scope
# project - number guessing game

# # namespace: local & global scope
# counter = 1
# def increase_counter():
#     counter = 3
#     print(f"inside: {counter}")
#     return counter
# increase_counter() # 3
# print(f"outside: {counter}") # 1

# # local scope
# def drink_potion():
#     potion_strength = 2 # variable with local scope
#     print(potion_strength)
# drink_potion() # 2
# # print(potion_strength) # returns an error

# # global scope
# player_hp = 10 # variable with global scope
# def eat_soup():
#     potion_strength = 2
#     print(player_hp)
# drink_potion() # 2

# def mainland():
#     def indoors(): # function with local scope
#         print("I'm indoors.")
#     indoors()
# mainland() # i'm indoors
# # indoors() # returns an error

# # ---------------------
# # does python have block scope? - no
# difficulty = 3
# if difficulty < 5:
#     enemy = 1
# print(enemy) # perfectly valid code for python

# ---------------------------
# how to modify a global variable
i = 0
def global_modifier():
    # i += 1 # returns an error
    # by using global modifier, we are able to modify global variable's value in a local scope
    global i
    i += 1
    print(i)
global_modifier() # 1
print(i) # 0; with global modifier, this will now also be modified to 1
# TIP: avoid modifying global scope variables
# do this instead:
j = 0
def this_is_the_way():
    print(f"inside: {j}")
    return j + 1
print(f"outside: {j}") # 0
print(f"modified j: {this_is_the_way()}") # 1

# ----------------------------------
# python constants and global scope
# global modifer is useful for defining python constants
# python constants are variables that can never be modified
# global constants are in all caps
NICKNAME = 'Jordan'



