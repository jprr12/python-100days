# randomization and python list
import random

# # coding exer day 4-1
# # coin toss bot
# # 1 - make a list of all possible outcomes
# coin_toss = ['heads', 'tails']
# # 2 - generate a random item from list using choice() function from random module
# ai_pick = random.choice(coin_toss)
# # 3 - prompt
# user_pick = input("heads or tails: ")
# # 4 - print this if picks matched
# if (user_pick == 'heads' and ai_pick == 'heads') or (user_pick == 'tails' and ai_pick == 'tails'):
    # print(f"Result is {ai_pick}. You got it!")
# # 5 - print this if picks didn't match
# elif (user_pick == 'heads' and ai_pick == 'tails') or (user_pick == 'tails' and ai_pick == 'heads'):
    # print(f"Result is {ai_pick}. Better luck next time.")
# # 6 - print this if typo
# else: print("Invalid input.")

# # coding exer day 4-2
# # banker roulette
# # ask user to input 5 names separated with a comma, code will pick one name randomly among the 5 names
# # 1 - prompt user
# names_string = input("Enter names separated with a comma(,): ")
# # 2 - make a list out of the names by using split()
# names = names_string.split(', ')
# # 3 - without using choice(), randomize the names using randint()
# random_name = random.randint(0,len(names)-1)
# # 4 - print result
# print(f"{names[random_name]} is going to buy the meal today!")

# # index errors and nested lists
# # sample nested list
# numbers = [0, 1, 2, 3, 4, 900]
# letters = ['a', 'b', 'x', 'y', 'j']
# alphanumeric = [numbers, letters]
# print(alphanumeric)
# print(alphanumeric[0][0])
# print(alphanumeric[0][1])
# print(alphanumeric[1][0])

# coding exer day 4-3
# treasure map
row1 = ['O', 'O', 'O']
row2 = ['O', 'O', 'O']
row3 = ['O', 'O', 'O']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# prompt user
position = input("Where do you want to put the treasure? ")
# 1 - separate the user input into two usable integer
row_map = int(position) // 10 # takes the 1st digit of the 2-digit input
index_map = int(position) % 10 # takes the 2nd digit of the 2-digit input
# 2 - replace the specific position in nested list with 'X'
map[index_map-1][row_map-1] = 'X'
# 3 - print result
print(f"{row1}\n{row2}\n{row3}")

