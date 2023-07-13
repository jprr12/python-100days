# secret auction program

# import art
import os

# adding entries to the auction dictionary
def add_entry(name, bid):
    auction[name] = bid

# sorting through the dictionary with the highest bid
def find_winner(bidding_record):
    highest_bid = 0
    highest_bidder = ''
    for bidder in bidding_record:
        bid_amt = bidding_record[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            highest_bidder = bidder
    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

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
# print(art.logo)
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
        find_winner(auction)
        break

