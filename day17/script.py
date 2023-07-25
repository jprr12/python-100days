# day 17 - benefits of OOP
# project - quiz project

# ===============================
# # creating your own class
# # declaration
# class User:
#     # empty
#     pass
# # create an object of that class
# user1 = User()
# # class names should be capitalized (PascalCase)

# ===============================
# # attributes, class constructors, __init__() function
# # adding attributes to your class
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
# john = User('john123', 'John')
# pablo = User('pablolous', 'Pablo')
# print(john.username)
# print(pablo.id)
# # # attributes - variables associated with an object
# # john.name = 'John'
# # john.age = 27
# # pablo.name = 'Pablo'
# # pablo.age = 31

# # class constructors
# class Pokemon:
#     # init function is used to initialize the attributes of a class
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
# charizard = Pokemon('Charizard', 'Fire/Flying')
# blastoise = Pokemon('Blastoise', 'Water') 
# print(charizard.type)
# print(blastoise.type)

# ===============================
# adding methods to a class
# methods are functions inside a class
class Car:
    def __init__(self):
        self.seats = 5
        self.tires = 4
    def race_mode(self):
        self.seats = 2

