# number guessing game project
from random import randint
import os
# from art import logo

def cls():
    '''clears screen for better UX'''
    os.system('cls' if os.name == 'nt' else 'clear')

def guess(difficulty):
    '''
    - checks what difficulty player chose
    - if then checks if they guessed the rnd number
    - if yes, they won; if no, attempt -= 1
    '''
    # initializes attempts depending on chosen difficulty
    if difficulty == 'easy':
        attempts_left = 10
    elif difficulty == 'hard':
        attempts_left = 5
    # looping until player wins or runs out of attempts
    while attempts_left > 0:
        print(f"Attempt/s left: {attempts_left}")
        player_guess = int(input("Make a guess: "))
        if player_guess == guess_this:
            print(f"You guessed right! The number is indeed {guess_this}!")
            break
        attempts_left -= 1
        if player_guess < guess_this:
            if guess_this - player_guess >= 10:
                print("Guess too low. Higher.")
            else:
                print("Higher.")
        else:
            if player_guess - guess_this >= 10:
                print("Guess too high. Lower.")
            else:
                print("Lower.")
        if attempts_left == 0:
            print(f"You reached your final attempt. You lose. The number is {guess_this}.")
            break

def game_start():
    '''
    - starts the game by initializing a rnd number b/w 1-100
    - asks the player for difficulty preference
    '''
    # print(guess_this) # for testing purposes only, remove this after testing
    # print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # looping to catch errors if player mistyped the difficulty choice
    right_difficulty = True
    while right_difficulty == True:
        difficulty = input("Choose difficulty (easy/hard): ")
        if (difficulty.lower() == 'easy') or (difficulty.lower() == 'hard'):
                guess(difficulty)
                break
        else:
            print("You can only pick between 'easy' and 'hard' difficulty.")

# looping the game until player
while input("Wanna play a game of number guessing? (y/n): ").lower() == 'y':
    cls()
    # initializing a random number
    guess_this = randint(1, 100)
    game_start()

