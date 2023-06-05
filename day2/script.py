# primitive data types/operations

# # strings
# greeting = "good morning!"
# # printing the 1st character of a strings
# print(greeting[0]) # 'g'; arrays always start with 0
# print(greeting[1]) # 'o'
# print(greeting[12]) # '!'
# print(greeting[-1]) # prints the last character
# # any text/characters inside quotes are strings

# # integer - whole numbers
# print(100) # prints 100
# print(100 + 111) # 211

# # float - decimals
# pi = 3.14159
# print(pi)

# # boolean - true/false
# correct = True
# notCorrect = False

# # type error, checking, conversion
# # type checking
# num_char = len(input("what is your name: "))
# print(type(num_char))

# # type conversion
# new_numChar = str(num_char) # converts to string
# print(type(new_numChar))

# # coding exer day2-1
# # data types
# # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# # 1 - prompt for a 2-digit number
# num = input("enter a 2-digit number: ")
# # 2 - convert each digit from string -> int
# digit1 = int(num[0])
# digit2 = int(num[1])
# total = digit1 + digit2
# # 3 - print output
# print(f"{digit1} + {digit2} = {total}")

# # mathematical operations
# # addition(+), subtraction(-), multiplication(*), division(/)
# # x raised to the power of y -> x**y
# print(2**3) # 8
# # PEMDAS

# # coding exer day2-2
# # bmi calculator
# # bmi = weight/height**2
# # 1 - prompt for height and weight
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 2 - calculate bmi
# bmi = float(weight)/(float(height)**2)
# # 3 - print output
# print(int(bmi))

# # number manipulation/f-strings
# # rounding floating points
# print(8/3) # 2.6666666..
# print(round(8/3)) # rounds the result up
# print(round(8/3, 2)) # rounds up to two decimal figures

# # floor division (//) -> rounds the result down to the nearest whole number

# # increment/decrement/value manipulation using * or /
# score = 0
# score += 1 # new score value -> 1
# print(score) # 1

# coding exer day2-3
# create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old
# 1 - prompt user's current age
age = input("What is your current age? ")
# 2 - subtract user's age to 90
diff = 90 - int(age)
# 3 - print result in days, weeks, and months
print(f"If you were to live up to 90, you only have {diff} years left, equivalent to {diff*365} days, {diff*52} weeks, and {diff*12} months.")
