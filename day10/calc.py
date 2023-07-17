# basic calculator app
from art import logo
import os

# function that clears screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# basic operation functions
# addition
def add(a, b):
    return a + b
# subtraction
def subtract(a, b):
    return a - b
# multiplication
def multiply(a, b):
    return a * b
# division
def divide(a, b):
    return round(a / b, 1)

# dictionary of operations
basic_op = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calc():
    print(logo)
    # prompt user for numbers and operation
    num1 = float(input("1st number: "))
    for symbol in basic_op:
        print(symbol)

    # perform operation
    cont = True
    while cont == True:
        operation = input("Choose an operation: ")
        num2 = float(input("Next number: "))

        if operation not in basic_op:
            print("Invalid operation. You can only use the four given operations.")
            continue
        else:
            for op in basic_op:
                if operation == op:
                    answer = basic_op[op](num1, num2)
                    print(f"{num1} {operation} {num2} = {answer}")
        decision_cont = input(f"Type 'y' to continue calculating with {answer}, type 'n' to stary a new calculation, or type 'e' to exit: ")
        if decision_cont.lower() == 'y':
            num1 = answer
            cls()
        elif decision_cont.lower() == 'n':
            cont = False
            cls()
            calc()
        else:
            print("Goodbye!")
            cont = False

calc()

