'''
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.

D
[['H', '2'], ['S', 'J'], ['D', 'A']]
nested list with pair lists, second of hearts, jack of spades, ash of diamonds
'''
import random

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')


def prompt(message):
    '''prompt message'''
    print(f"=> {message}")

def initialize_deck():
    '''shuffle all cards'''
    shuffle_deck = [f"{value}{suit}" for value in VALUES for suit in SUITS]
    random.shuffle(shuffle_deck)
    return shuffle_deck

# Calculating cards value

def total(cards):
    '''calculates the value of all cards'''
    sum_val = 0
    for card in cards:
        value = card[:-1]

        if value == 'A':
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # correct Aces value depending on sum_val
    for card in cards:
        value = card[:-1]
        if sum_val <= 21:
            break
        if value == 'A':
            sum_val -= 10

    return sum_val

# - Ask player to hit or stay.
# - If stay, stop asking.
# - Otherwise, go to #1.

def busted(cards):
    '''returns true when cards value is above 21'''
    return total(cards) > 21

def detect_result(cards_dealer,cards_player):
    '''reads the result for both the dealer and the player'''
    player_total = total(cards_player)
    dealer_total = total(cards_dealer)

    if player_total > 21:
        return 'PLAYER BUSTED'
    if dealer_total > 21:
        return 'DEALER BUSTED'
    if dealer_total < player_total:
        return 'PLAYER'
    if dealer_total > player_total:
        return 'DEALER'

    return 'TIE'

def display_results(cards_dealer, cards_player):
    '''displays the result for both the dealer and the player'''
    result = detect_result(cards_dealer, cards_player)

    match result:
        case 'PLAYER_BUSTED':
            prompt('You busted! Dealer wins!')
        case 'DEALER_BUSTED':
            prompt('Dealer busted! You win!')
        case 'PLAYER':
            prompt('You win!')
        case 'DEALER':
            prompt('Dealer wins!')
        case _:
            prompt("It's a tie!")

def play_again():
    '''help function asking to play again'''
    while True:
        prompt('Do you want to play again? (y or n)')
        answer = input().strip().lower()

        if answer in ['yes', 'y']:
            return True

        if answer in ['no', 'n']:
            return False

        prompt('invalid input, choose y or n')

def pop_two_from_deck(deck):
    '''take two cards from deck'''
    return [deck.pop(), deck.pop()]

def hand(cards):
    '''show all cards'''
    return ', '.join(cards)


prompt('Welcome to Twenty-One!')
while True:

    #initial deal
    deck = initialize_deck()
    player_cards = pop_two_from_deck(deck)
    dealer_cards = pop_two_from_deck(deck)

    prompt(f"dealer has {dealer_cards[0]} and another card")
    prompt(f"You have: {player_cards[0]} and {player_cards[1]}")
    prompt(f"Your total is: {total(player_cards)}")

    # player turn
    while True:
        prompt("Would you like to hit or stay, h or s?")
        player_choice = input()
        if player_choice not in ['h', 's']:
            prompt("Sorry, choose between 'h' or 'y'.")
            continue

        if player_choice == 'h':
            player_cards.append(deck.pop())
            prompt("You choose to hit!")
            prompt(f"Your cards are now: {hand(player_cards)}")
            prompt(f"Your total is: {total(player_cards)}")

        if player_choice == 's' or busted(player_cards):
            break

    if busted(player_cards):
        display_results(dealer_cards, player_cards)
        if play_again():
            continue

    else:
        prompt(f"You stay at {total(player_cards)}")

    # dealer turn:
    prompt("Dealer's turn...")

    while total(dealer_cards) < 17:
        prompt("Dealer hits")
        dealer_cards.append(deck.pop())
        prompt(f"Dealer's cards are now: {hand(dealer_cards)}")

    if busted(dealer_cards):
        prompt(f"Dealer total is now: {total(dealer_cards)}")
        display_results(dealer_cards, player_cards)
        if play_again():
            continue

    else:
        prompt(f"Dealer stays at {total(dealer_cards)}")

    ## at this point both player and dealer stay - compare cards

    print('=============')
    prompt(f"Dealer has {hand(dealer_cards)}, for a total of: {total(dealer_cards)}")
    prompt(f"Player has {hand(dealer_cards)}, for a total of: {total(player_cards)}")
    print('=============')

    display_results(dealer_cards, player_cards)

    if play_again():
        continue

prompt('Thank you for playing Twenty-One!')
