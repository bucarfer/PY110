'''Generic description
Display the initial empty 3x3 board.
Ask the user to mark a square.
Computer marks a square.
Display the updated board state.
If it's a winning board, display the winner.
If the board is full, display tie.
If neither player won and the board is not full, go to #2
Play again?
If yes, go to #1
Goodbye!
'''

# Modules imported
import os
import random

#0. set up CONSTANTS to avoid "magic numbers"
INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
FINAL_WINNER = 5

#1. step 1. function to build the board (3x3)

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def display_board(board):
     os.system('clear') # clears board with module system

     prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
     print('     |     |')
     print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
     print('     |     |')
     print('-----+-----+-----')
     print('     |     |')
     print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
     print('     |     |')
     print('-----+-----+-----')
     print('     |     |')
     print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
     print('     |     |')
     print('')

# initialize_board = {
#     1: ' ', # top left
#     2: ' ', # top center
#     3: ' ', # top right
#     4: ' ', # middle left
#     5: ' ', # middle center
#     6: ' ', # middle right
#     7: ' ', # bottom left
#     8: ' ', # bottom center
#     9: ' ', # bottom right
# }

##2. function to ask player to choose square

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER] # valid choices

## TT bonus 1. Improve Join

def join_or(my_list, connector=',', end_connector='or'):
    if not my_list:
        return ""

    elif len(my_list) == 1:
        return str(my_list[0])

    elif len(my_list) == 2:
        return f"{my_list[0]} {end_connector} {my_list[1]}"

    return f"{connector.join(str(x) for x in my_list[:-1])}{connector} {end_connector} {my_list[-1]}"

# test cases
# print(join_or([1, 2, 3]))               # => "1, 2, or 3"
# print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3" ';' instead of ','
# print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3" different separator
# print(join_or([]))                      # => ""
# print(join_or([5]))                     # => "5"
# print(join_or([1, 2]))                  # => "1 or 2" no comma

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break # valid number

        prompt("Sorry, that's not a valid choice.") # no need for else clause

    board[int(square)] = HUMAN_MARKER

##3. function for computer to choose square

def computer_chooses_square(board):
    if empty_squares(board) == []:
        return # stops lines after here from running (no need to return anything)
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

##4. loops for keep playing until someone wins or full_board

def someone_won(board):
    return bool(detect_winner(board))

def board_full(board):
    return empty_squares(board) == []

##5. function to determine when someone wins

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
        [1, 5, 9], [3, 5, 7]             # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line # unpacking list
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None # if previous conditions are not met (no one wins)

## TT bonus 2. Keep Score

def keep_score(winner, player_count, computer_count):
    if winner == 'Player':
        player_count += 1
    elif winner == 'Computer':
        computer_count += 1

    return player_count, computer_count

def detect_final_winner(player_count, computer_count):
    if player_count == FINAL_WINNER:
        return 'Player'

    if computer_count == FINAL_WINNER:
        return 'Computer'

    else:
        return None

## main function code

def play_tic_tac_toe():
    while True:
        board = initialize_board()

    # player and machines loop chooses
        while True:
            display_board(board)

            player_chooses_square(board)
            if someone_won(board) or board_full(board): # to break loop
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board): # to break loop
                break

        display_board(board)

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt(f"It's a tie!")

    ## TT bonus 2. Keep Score

        player_count = 0
        computer_count = 0

        player_count, computer_count = keep_score(detect_winner(board), player_count, computer_count)
        prompt(f"First to win 5 games is the final winner \n player wins:{player_count}. Computer wins:{computer_count}")

        if detect_final_winner(player_count, computer_count):
        prompt(f"{detect_final_winner(player_count, computer_count)} is the final winner!")

    ## end of TT bonus 2.

        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break

    prompt("Thanks for playing Tic Tac Toe!")

play_tic_tac_toe()