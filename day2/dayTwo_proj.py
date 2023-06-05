# tip calculator
print("This is a tip calculator.\n")
# 1 - prompt for total bill
total_bill = float(input("total bill: "))
# 2 - prompt for percentage of tip
tip_percent = (float(input("percentage of tip you want to give: "))/100)+1
# 3 - prompt for number of people splitting the bill
peeps = int(input("number of people splitting the bill: "))
# 4 - calculate tip, print result
pay_tip = (total_bill/peeps) * tip_percent
rounded = "{:.2f}".format(pay_tip) # formatting result to 2 decimal places
print(f"Each person should pay ${rounded}.")