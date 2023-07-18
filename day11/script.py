# blackjack capstone project
import random
import os
from art import logo

# initialize deck so that it can be reused in various functions
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10]

def cls():
    '''clears the screen for better UX'''
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card(deck):
    '''return a random card from the cardpool'''
    return random.choice(deck)

def calc_score(hand):
    '''calculates the score in a players hand'''
    # checks if the opening hand is blackjack
    if (sum(hand) == 21) and len(hand) == 2:
        return 21
    # check if hand has an ace and need to apply ace rule
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def winner(user_cards, ai_cards):
    '''determines the winner of the game and returns a statement'''
    # *could use further optimization
    print(f"Your cards: {user_cards}, final score: {calc_score(user_cards)}")
    print(f"Dealer's final hand: {ai_cards}, final score: {calc_score(ai_cards)}")
    if calc_score(user_cards) <= 21:
        if ((calc_score(ai_cards) == 21) and (calc_score(user_cards) == 21)) or (calc_score(ai_cards) == calc_score(user_cards)):
            return "It's a draw."
        elif calc_score(user_cards) > calc_score(ai_cards):
            if calc_score(user_cards) == 21:
                return "Blackjack! You win!"
            else:
                return "You win!"
        elif calc_score(ai_cards) > 21:
            return "Dealer went over. You win!"
        else:
            return "You lose."
    
    elif (calc_score(user_cards) > 21):
        return "You went over. You lose."
    elif calc_score(ai_cards) == 21:
        return "Dealer won by blackjack! You lose."

def start():
    '''start the game by dealing 2 cards
    game ends if player or computer scores 21, or if player goes over 21'''
    print(logo)
    # initialize player and computer hand
    user_cards = []
    ai_cards = []
    # deal 2 random cards to both players
    for i in range(2):
        user_cards.append(deal_card(cards))
        ai_cards.append(deal_card(cards))
    while (calc_score(user_cards) <= 21):
        # ends the game if either player scored blackjack or player went over
        if (calc_score(user_cards) == 21) or (calc_score(ai_cards) == 21) or (calc_score(user_cards) > 21):
            print(winner(user_cards, ai_cards))
            break
        # shows the first 2 cards for player and the first card for computer
        print(f"Your cards: {user_cards}, current score: {calc_score(user_cards)}")
        print(f"Dealer's first card: {ai_cards[0]}")
        # asks player to hit or pass
        play_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        if play_pass.lower() == 'n':
            # if player passes, computer draws cards until they go over 16
            while calc_score(ai_cards) <= 16:
                ai_cards.append(deal_card(cards))
                if calc_score(ai_cards) > 16:
                    break
            print(winner(user_cards, ai_cards))
            break
        elif play_pass.lower() == 'y':
            # if player hits, they draw a random card
            user_cards.append(deal_card(cards))
            # checks if player goes over 21; if not, play continues
            if calc_score(user_cards) > 21:
                # if player goes over 21, computer will draw cards until they go over 16
                ai_cards.append(deal_card(cards))
                while calc_score(ai_cards) <= 16:
                    ai_cards.append(deal_card(cards))
                    if calc_score(ai_cards) > 16:
                        break
                print(winner(user_cards, ai_cards))
                break
            # if player scores blackjack, game ends
            elif calc_score(user_cards) == 21:
                print(winner(user_cards, ai_cards))
                break

# continue asking player if they want another game after each and every match
while input("Want to play a game of blackjack? y/n: ").lower() == 'y':
    cls()
    start()

