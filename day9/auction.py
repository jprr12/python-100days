# secret auction program

import art
import os

# adding entries to the auction dictionary
def add_entry(name, bid):
    auction[name] = bid

# sorting through the dictionary with the highest bid
def winner():
    all_bid = []
    # store all bid values in the list all_bid
    for item in auction:
        all_bid.append(auction[item])
    # take the highest bid
    highest_bid = max(all_bid)
    # finding the name of the highest bidder
    highest_bidder = None
    for key, value in auction.items():
        if value == highest_bid:
            highest_bidder = key
            break
    # display the auction winner
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

# main menu
def menu():
    name = input("What is your name: ")
    bid = int(input("What is your bid ($): "))
    if name in auction:
        print(f"{name} is already in the bidding list.")
    else:
        add_entry(name, bid)
# ------------------------------------
# art for improved UX
print(art.logo)
print("Welcome to the secret auction program.")
auction = {}

menu()
again = True
while again == True:
    try_again = input("Are there any other bidders (yes or no): ")
    if try_again.lower() == 'yes':
        os.system('cls')
        menu()
    else:
        winner()
        break

