# password generator
# using random, lists, for-loops, append(), join() w/ delimiter, shuffle()
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# 1 - prompt user
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# 2 - generate a random letter/symbol/number for the password
# 2a - make a list to save the generated random l/s/n
random_letters = []
random_symbols = []
random_numbers = []
# 2b - generate random l/s/n using choice()
for l in range(0, nr_letters):
    random_letters.append(random.choice(letters))
for s in range(0, nr_symbols):
    random_symbols.append(random.choice(symbols))
for n in range(0, nr_numbers):
    random_numbers.append(random.choice(numbers))
# 2c - combine all the generated l/s/n into one list
password = random_letters + random_numbers + random_symbols
# 3 display the generated random password (unshuffled) as a string using a delimiter
delimiter = ''
unshuffled_pw = delimiter.join(password)
print(unshuffled_pw)
# 4 - shuffle the list to create the final password and print result
random.shuffle(password)
final_password = delimiter.join(password)
print(final_password)


