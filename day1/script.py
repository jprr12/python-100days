# string manipulation/variables

# print() function
print("hello world")

# new line (\n)
print("this is above\nthis is below")

# string concatenation
print("hello" + " " + "bro") # hello bro
print("hello" + "bro") # hellobro

# coding exer day1-2
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print("e.g. print(\"Hello\" + \"world\")")
print("New lines can be created with a backlash and n.")

# input() function
print("Hello " + input("What is your name? ") + "! Nice to meet you!")

# coding exer day1-3
# 1 - prompt user for name
name = input("Enter your name: ")
# 2 - len() function calculates the length of a string
print(f"Nice to meet you, {name}! Your name has {len(name)} characters.")

# python variables
# coding exer day1-4
# write a program that switches the values stored in the variables a and b
# 1 - prompt user for value of a, b
a = input("a: ")
b = input("b: ")
# 2- swapping algorithm (lol)
c = a
a = b
b = c
# - print the result
print("a: " + a)
print("b: " + b)