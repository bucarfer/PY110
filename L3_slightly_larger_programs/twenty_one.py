'''
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= MAX_DEALER_CARDS_VALUE
6. If dealer busts, player wins.
7. Compare cards and declare winner.

D
[['H', '2'], ['S', 'J'], ['D', 'A']]
nested list with pair lists, second of hearts, jack of spades, ash of diamonds
'''

## fix when someone busted -> asks to play again and doesn't update the final result

import random

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
MAX_CARDS_VALUE = 21
MAX_DEALER_CARDS_VALUE = 17
FINAL_WINNER = 5

# Global score counters
player_count = 0
dealer_count = 0

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
        if sum_val <= MAX_CARDS_VALUE:
            break
        if value == 'A':
            sum_val -= 10

    return sum_val

def busted(total_value):
    '''returns true when cards value is above MAX_CARDS_VALUE'''
    return total_value > MAX_CARDS_VALUE

def detect_result(player_total, dealer_total):
    '''reads the result for both the dealer and the player'''

    if player_total > MAX_CARDS_VALUE:
        return 'PLAYER BUSTED'
    if dealer_total > MAX_CARDS_VALUE:
        return 'DEALER BUSTED'
    if dealer_total < player_total:
        return 'PLAYER'
    if dealer_total > player_total:
        return 'DEALER'

    return 'TIE'

def display_results(player_total, dealer_total):
    '''displays the result for both the dealer and the player'''
    result = detect_result(player_total, dealer_total)

    match result:
        case 'PLAYER BUSTED':
            prompt('You busted! Dealer wins!')
        case 'DEALER BUSTED':
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

## count result for final winner

def keep_score(winner):
    '''keeps score'''
    global player_count, dealer_count

    if winner == 'DEALER BUSTED' or winner == 'PLAYER':
        player_count += 1
    elif winner == 'PLAYER BUSTED' or winner == 'DEALER':
        dealer_count += 1

def detect_final_winner():
    '''detects who is the final winner'''

    if player_count == FINAL_WINNER:
        prompt('You are the final winner!')

    if dealer_count == FINAL_WINNER:
        prompt('The dealer is the final winner!')

def final_winner_operation(player_total, dealer_total):
    '''counts games for final winner and shows result'''
    winner = detect_result(player_total, dealer_total)
    keep_score(winner)

    prompt(f"First to win {FINAL_WINNER} games is the final winner")
    prompt(f"player wins:{player_count} dealer wins:{dealer_count}")

    detect_final_winner()

def reset_or_exit_if_final_winner():
    '''resets count if final winner met'''
    global player_count, dealer_count

    if player_count == FINAL_WINNER or dealer_count == FINAL_WINNER:
        if not play_again():
            return True

        player_count = 0
        dealer_count = 0

    return False

# ========================
## MAIN  LOOP
# ========================

prompt('Welcome to Twenty-One!')

while True:

    #initial deal
    deck = initialize_deck()
    player_cards = pop_two_from_deck(deck)
    dealer_cards = pop_two_from_deck(deck)

    player_total = total(player_cards)
    dealer_total = total(dealer_cards)

    prompt(f"dealer has {dealer_cards[0]} and an unknown card")
    prompt(f"You have: {player_cards[0]} and {player_cards[1]}")
    prompt(f"Your total is: {player_total}")

    # Player turn
    while True:
        prompt("Would you like to hit or stay, h or s?")
        player_choice = input().strip().lower()

        if player_choice not in ['h', 's']:
            prompt("Sorry, choose between 'h' or 's'.")
            continue

        if player_choice == 'h':
            player_cards.append(deck.pop())
            player_total = total(player_cards)

            prompt("You choose to hit!")
            prompt(f"Your cards are now: {hand(player_cards)}")
            prompt(f"Your total is: {player_total}")

        if player_choice == 's' or busted(player_total):
            break

    if busted(player_total):
        display_results(player_total, dealer_total)
        final_winner_operation(player_total, dealer_total)

        if reset_or_exit_if_final_winner():
            break
        if play_again():
            continue

    else:
        prompt(f"You stay at {player_total}")

    # dealer turn:
    prompt("Dealer's turn...")

    while dealer_total < MAX_DEALER_CARDS_VALUE:
        dealer_cards.append(deck.pop())
        dealer_total = total(dealer_cards)
        prompt("Dealer hits")
        prompt(f"Dealer's cards are now: {hand(dealer_cards)}")

    if busted(dealer_total):
        prompt(f"Dealer total is now: {dealer_total}")
        display_results(player_total, dealer_total)
        final_winner_operation(player_total, dealer_total)

        if reset_or_exit_if_final_winner():
            break

        if play_again():
            continue

    else:
        prompt(f"Dealer stays at {dealer_total}")

    ## at this point both player and dealer stay - compare cards
    print('=============')
    prompt(f"Dealer has {hand(dealer_cards)}, for a total of: {dealer_total}")
    prompt(f"Player has {hand(player_cards)}, for a total of: {player_total}")
    print('=============')

    ## Update and show result for final winner
    display_results(player_total, dealer_total)
    final_winner_operation(player_total, dealer_total)

    # handles if any player has reached FINAL_WINNER
    if reset_or_exit_if_final_winner():
        break

prompt('Thank you for playing Twenty-One!')
