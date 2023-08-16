# day 26 - list and dictionary comprehension
# project - nato phoenetic alphabet

# # creating a list with list comprehension
# # list comprehension - syntax
# # eg1
# numbers = [1, 2, 3, 4]
# doubled_num = [n*2 for n in numbers]
# # eg2
# name = 'marai'
# char_list = [c for c in name]
# print(char_list)
# # challenge - create a range, use list comprehension to double
# doubled_range = [n*2 for n in range(1,5)]
# print(doubled_range)
# # conditional list comprehension
# # eg1
# cond_lc = [n/2 for n in range(0,5) if n != 2]
# print(cond_lc)
# # eg2
# cond_lc = [n for n in range(0,21) if n%2 == 0]
# print(cond_lc)
# # challenge
# # make a list from names that contains 5 chars or more
# # transform the names to uppercase
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# modified_names = [n.upper() for n in names if len(n) > 4]
# print(modified_names)

# ===========================================================
# # interactive coding exer - squaring numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_nums = [n**2 for n in numbers]
# print(squared_nums)

# # interactive coding exer - filtering even numbers
# even = [n for n in numbers if n%2 == 0]
# print(even)

# ===========================================================
# # interactive coding exer - data overlap
# with open('file1.txt', 'r') as file1:
#     numbers_1 = file1.readlines()
# with open('file2.txt', 'r') as file2:
#     numbers_2 = file2.readlines()

# result = [int(n) for n in numbers_1 if n in numbers_2]
# print(result)

# ===========================================================
# apply list comprehension to states game
# missing_states = [state for state in all_states if state not in guessed_states]

# ===========================================================
# # dictionary comprehension
# import random
# names = ['Harry', 'Ron', 'Hermione', 'Neville', 'Draco']
# score_dict = {name:random.randint(60, 99) for name in names}
# print(score_dict)

# passed_students = {name:score for (name, score) in score_dict.items() if score > 75}
# print(passed_students)

# ===========================================================
# # interactive coding exer - dictionary comprehension 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence_list = sentence.split()
# result = {word:len(word) for word in sentence_list}
# print(result)

# # interactive coding exer - dictionary comprehension 2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day:round(temp*(9/5)+32, 1) for (day, temp) in weather_c.items()}
# print(weather_f)

# ===========================================================
# iterating over pandas data frame
import pandas

score_dict = {
    'student': ['Ron', 'Hermione', 'Harry'],
    'score': [79, 96, 88]
}

score_df = pandas.DataFrame(score_dict)
print(score_df)

# built in pandas loop
for (index, row) in score_df.iterrows():
    # print(index)
    # print(row)
    print(row.student)
    # print(row.score)
    # if row.student == 'Harry':
    #     print(row.score)

