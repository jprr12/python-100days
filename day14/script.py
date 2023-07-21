# higher lower game project
import random
from game_data import data
import os
# import art # optional

def cls():
    '''clear screen for better UX'''
    os.system('cls' if os.name == 'nt' else 'clear')

def higher_ff(celebA, celebB):
    '''returns celebrity with the higher follower count'''
    if celebA['follower_count'] > celebB['follower_count']:
        return celebA
    else:
        return celebB

def game_start(celebA, celebB):
    '''takes user input and returns the celebrity dictionary from the data list'''
    # asking user to guess who has the higher follower count
    print(f"Compare A: {celebA['name']}, {celebA['description']} from {celebA['country']}.")
    print(f"Against B: {celebB['name']}, {celebB['description']} from {celebB['country']}.\n")
    player_guess = input("Who has more followers? (A/B): ").lower()
    if player_guess == 'a':
        return celebA
    else:
        return celebB
        
# initializing score
score = 0
# randomizing a celebrity from the data list
celebrity_A = random.choice(data)
game_on = True
while game_on == True:
    # randomizing a different celebrity
    celebrity_B = celebrity_A
    while celebrity_B == celebrity_A:
        celebrity_B = random.choice(data)
    # start game
    if game_start(celebrity_A, celebrity_B) == higher_ff(celebrity_A, celebrity_B):
        cls()
        score += 1
        celebrity_A = higher_ff(celebrity_A, celebrity_B)
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Wrong! Final score: {score}")
        game_on = False


