# dictionaries and nesting
# project - secret auction program

# # python dictionaries
# # {key1 : value1, key2 : value2, ... keyX : valueX}
# programming_dict = {
#     'bug': 'an error in a program that prevents the program from running as expected.',
#     'function': 'a piece of code that you can easily call over and over again.',
#     'loop': 'the action of doing something over and over again.',
#     1: 'one'
# }
# # calling items in a dictionary
# print(programming_dict['loop']) # prints value for 'loop'
# print(programming_dict[1]) # one

# # adding new item/s in a dictionary
# programming_dict['new item'] = 214
# print(programming_dict['new item']) # 214

# # creating an empty dictionary
# empty_dict = {}

# # wiping an existing dictionary
# programming_dict = {}
# print(programming_dict) # empty

# # editing an item in a dictionary
# programming_dict['bug'] = 'an insect'
# print(programming_dict['bug']) # value changed

# # looping through a dictionary
# for item in programming_dict:
#     print(item) # prints keys only
#     print(programming_dict[item]) # prints values only

# # -----------------------
# # coding exer day 9-1
# # grading program
# # You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# # Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
# # grade criteria : 100-91 > outstanding, 90-81 > exceeds expectations, 80-71 > acceptable 70 or lower > fail
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 1 - create an empty dictionary student_grades
# student_grades = {}
# # 2 - loop through the student_scores dictionary and convert the scores to the grade criteria, then store it in student_grades 
# for item in student_scores:
#     student_grades = student_scores
#     if student_scores[item] >= 91:
#         student_grades[item] = "outstanding"
#     elif student_scores[item] >= 81 and student_scores[item] <= 90:
#         student_grades[item] = "exceeds expectations"
#     elif student_scores[item] >= 71 and student_scores[item] <= 80:
#         student_grades[item] = "acceptable"
#     else:
#         student_grades[item] = "fail"
# # print result
# print(student_grades)

# # --------------------------------
# # nesting lists and dictionaries
# capitals = {
#     'France': 'Paris',
#     'Germany': 'Berlin'
# }

# # nesting a list in a dictionary
# travel_log = {
#     'France': ['Paris', 'Lille', 'Dijon'],
#     'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
# }

# # nesting dictionary in a dictionary
# travel_log2 = {
#     'France': {'cities visited': ['Paris', 'Marseilles', 'Nice'], 'total visits': 12},
#     'Philippines': {'cities visited': ['Manila', 'Naga', 'Legazpi', 'Baguio'], 'total visits': 9}
# }

# # nesting dictionaries in a list
# my_list = [capitals, travel_log, travel_log2]
# my_list2 = [
#     {
#         'country': 'France',
#         'cities visited': ['Paris', 'Marseilles', 'Nice'],
#         'total visits': 12
#     },
#     {
#         'country': 'Philippines',
#         'cities visited': ['Manila', 'Naga', 'Legazpi', 'Baguio'],
#         'total visits': 9
#     },
#     {
#         'country': 'Australia',
#         'cities visited': ['Melbourne', 'Sydney', 'Canberra'],
#         'total visits': 3
#     }
# ]

# ------------------------------------------------
# coding exer day 9-2
# dictionary in a list
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# 1 - make a function add_new_country() that adds new countries to the travel_log
def add_new_country(country, visits, cities):
    # this function adds new entries to the list travel_log
    travel_log.append(
        {
            "country": country,
            "visits": visits,
            "cities": cities
        }
        )

# 2 - call function
add_new_country("Russia", 2, ['Moscow', 'Saint Petersburg', ])
# 3 - print result
print(travel_log)

