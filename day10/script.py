# functions with outputs
# day 10 project - calculator app

# def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())
# format_name('jOHn', 'paUL')

# def format_name(f_name, l_name):
    # formated_fname = f_name.title()
    # formated_lname = l_name.title()
    # print(f"{formated_fname} {formated_lname}")
# format_name('jOHn', 'pAuL')

# # using return instead
# def format_name(f_name, l_name):  
#     formated_fname = f_name.title()
#     formated_lname = l_name.title()
#     return f"{formated_fname} {formated_lname}"
# print(format_name('tIAnnA', 'crowNGUARd'))

#---------------------------
# # multiple return values
# def format_name(f_name, l_name):
#     if f_name == '' or l_name == '':
#         return "Error"
#     else:
#         formated_fname = f_name.title()
#         formated_lname = l_name.title()
#         return f"{formated_fname} {formated_lname}"
# print(format_name(input("First name: "), input("Last name: ")))

# ---------------------------
# coding exer day 10-1
# days in month
# create a function that returns the number of days in a month given month and year
# function that determines if a year is a leap year
# if leap year -> true, else -> false
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# function that will take year and month as input 
# will output total days in that year/month
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # check if leap=true
    if is_leap(year) == True:
        # change febraury to have 29 days if leap=true
        month_days[1] = 29
        return month_days[month-1]
    else:
        return month_days[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# ----------------------------
# # docstrings
# def myFunction():
#     """this is a docstring. function documentation is important."""
#     print("first docstring. you won't see it though.")
# myFunction()

# ---------------------------


