# hangman in python
# with for/while loops, if-elif-else, lists, strings, range, modules

import random

# breaking the hangman problem into a flowchart
# 1 - generate a random word
# 2 - replace the random word with blanks
# 3 - prompt user for a single letter
# 4 - if player guessed a letter correctly, replace the blank with the letter
# 5 - if player guessed incorrectly, or typed in more than one letter, or typed a non-alphabetical character, player loses a life
# 6 - if player runs out of life, player loses the game and the word is revealed
# 7 - if all blanks are filled, player wins
# 8 - if blanks aren't filled, go back to 3

# # challenge 1
# word_list = ["aardvark", "baboon", "camel"]
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = random.choice(word_list)
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("guess a letter: ").lower()
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print('correct')
#     else:
#         print("wrong")

# # challenge 2
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# print(f"Hint: {chosen_word}")
# #TODO-1: - Create an empty List called display.
# display = []
# #For each letter in the chosen_word, add a "_" to 'display'.
# for letter in chosen_word:
#     display.append("_")
# guess = input("Guess a letter: ").lower()
# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# i = 0
# for letter in chosen_word:
#     if letter == guess:
#         display[i] = guess
#         i += 1
#     else:
#         i += 1
# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# delimiter = ''
# display_str = delimiter.join(display)
# print(display_str)

# # challenge 3 - looping the whole process + guessing if player won
# # my solution:
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# while '_' in display:
#     guess = input("Guess a letter: ").lower()
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     print(display)
#     # saying the player won after guessing all the letters in hosen_word
#     if '_' not in display:
#         print("Congratulations, you win!")
#         break
#     else: 
#         continue

# # challenge 3 - keeping track of the player's 'life'
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
# #Set 'lives' to equal 6.
# lives_left = 6
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1. 
#     #If lives goes down to 0 then the game should stop and it should print "You lose."
#     if guess not in chosen_word:
#         lives_left -= 1
#         if lives_left == 0:
#             print("Game over. You lose.")
#             break
#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#     print(stages[lives_left])

# challenge 5 - improving UX
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
import hangman_art
import wordbank
word_list = wordbank.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("You already guessed that letter.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"{guess} is not in the word.")
        if lives == 0:
            end_of_game = True
            print("Game over. You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You got the word. You win!")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])

