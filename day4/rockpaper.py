# day 4 project - rock paper scissors
import random

print("Let's play rock paper scissors!")

# 1 - randomize computer choice
decision = ['rock', 'paper', 'scissors']
ai_choice = random.choice(decision)

# 2 - prompt user
user = input("Type 1 for rock, 2, for paper, 3 for scissors: ")

# 3 - determine winner
# 3a - output if user picked out of range
if (int(user) > len(decision)) or int(user) <= 0:
    print("Invalid choice.")
else:
    # 3b - output if user picked within range
    user_choice = decision[int(user)-1]
    if user_choice == ai_choice:
        print(f"You played {user_choice} and computer played {ai_choice}. It's a tie!")
    elif ((user_choice == 1 and ai_choice == 'scissors') or (user_choice == 2 and ai_choice == 'paper') or (user_choice == 3 and ai_choice == 'rock')):
        print(f"You played {user_choice} and computer played {ai_choice}. You win!")
    else: print(f"You played {user_choice} and computer played {ai_choice}. Computer wins!")