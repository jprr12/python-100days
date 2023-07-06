# python loops

# # for loop
# # syntax: for 'item' in [list]: --code
# sampList = ['a', 'B', 1, 5, 100]
# for sampItem in sampList:
#     print(sampItem) # prints an item in the list until every item in the list is printed

# # coding exer day 5-1
# # average height
# # 1 - prompt user for height
# student_heights = input("Input a list of student heights separated with a space (cm): ").split() # splits input from space
# # 2 - save input in a list
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 3 - get average
# sum = 0
# for i in student_heights: # sum of heights
#     sum += i
# ave_height = sum/(len(student_heights)) # average formula
# # 4 - print result
# print(round(ave_height))

# # coding exer day 5-2
# # high score
# # 1 - prompt user for student scores
# student_scores = input("Input a list of student scores ").split()
# # 2 - save input in a list
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 3 - find the highest score in the list (without using max)
# highest_score = student_scores[0]
# for i in student_scores:
#     if i > highest_score:
#         highest_score = i
# # 4 - print result
# print(f"Highest score: {highest_score}")

# # for-loop and range() function
# for r in range(1, 10):
#     print(r) # prints 1 2 ... 9, excluding 10
# for s in range(1, 11, 2): # third parameter is for the number of steps
#     print(s) # 1 3 5 .. 9

# # coding exer day 5-3
# # adding even numbers from 1 to 100
# # 1 - make a list that contains all numbers from 1 - 100
# numbers = []
# for n in range(1, 101):
#     numbers.append(n)
# evens = []
# # 2 - save all even numbers in a list
# for e in numbers:
#     if e % 2 == 0:
#         evens.append(e)
# # 3 - get the sum of all the even numbers in the list (without using sum())
# print(sum(evens))

# # 5-3 - alternate shorter solution
# even_total = 0
# for e in range(1, 101):
#     if e % 2 == 0:
#         even_total += e
# print(even_total)

# # coding exer 5-4
# # fizzbuzz
# # print all numbers from 1-100; if divisible by 3, print fizz; divisible by 5, print buzz; if divisible by 15, print fizzbuzz
# # 1 - make a list that contains all numbers from 1 - 100
# numbers = []
# for n in range(1, 101):
#     numbers.append(n)
# # 2 - change the items on the list that are divisible by 3, 5, or 15
# for i in range(0, 100):
#     if (i + 1) % 15 == 0:
#         numbers[i] = 'FizzBuzz'
#     elif (i + 1) % 3 == 0:
#         numbers[i] = 'Fizz'
#     elif (i + 1) % 5 == 0:
#         numbers[i] = 'Buzz'
# # 3 - print result
# for e in numbers:
#     print(e)

# alternate 5-4 without using lists
for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: print(number)

