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

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
        [1, 5, 9], [3, 5, 7]             # diagonals
    ]

# 'player', 'computer', or 'choose'
FIRST_TO_MOVE = 'choose'

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

def join_or(my_list, connector=', ', end_connector='or'):
    if not my_list:
        return ""

    elif len(my_list) == 1:
        return str(my_list[0])

    elif len(my_list) == 2:
        return f"{my_list[0]} {end_connector} {my_list[1]}"

    return f"{connector.join(str(x) for x in my_list[:-1])}{connector}{end_connector} {my_list[-1]}"

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

##3. Function for computer to choose square
    # refer to bonus 3 and 4

##4. loops for keep playing until someone wins or full_board

def someone_won(board):
    return bool(detect_winner(board))

def board_full(board):
    return empty_squares(board) == []

##5. function to determine when someone wins

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line # unpacking list
        if (board[sq1] == board[sq2] == board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == board[sq2] == board[sq3] == COMPUTER_MARKER):
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

def play_again():
    while True:
        prompt("Play again? (y or n)")
        answer = input().strip().lower()

        if answer in ['y', 'yes']:
            return True

        if answer in ['n', 'no']:
            return False

        else:
            prompt('invalid input, choose yes or no')


## TT bonus 3 and 4. Computer AI defense and offense

def offense_or_defense(board):
    block_candidate = None # initialize first

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        possible_winner = [board[sq1], board[sq2], board[sq3]]

        # offense -> complete computer markers
        if possible_winner.count(COMPUTER_MARKER) == 2 and possible_winner.count(INITIAL_MARKER) == 1:
            if board[sq1] == INITIAL_MARKER: return sq1
            if board[sq2] == INITIAL_MARKER: return sq2
            if board[sq3] == INITIAL_MARKER: return sq3

        # defense -> remember block, but keep scanning to prioritize offense
        if possible_winner.count(HUMAN_MARKER) == 2 and possible_winner.count(INITIAL_MARKER) == 1:
            if board[sq1] == INITIAL_MARKER: block_candidate = sq1
            elif board[sq2] == INITIAL_MARKER: block_candidate = sq2
            else: block_candidate = sq3

    return block_candidate # if no offense, maybe block, else None

# Function for computer to choose square
def computer_chooses_square(board):
    if not empty_squares(board):
        return
    # stops lines after here from running (no need to return anything)

    # offense or defense
    sq = offense_or_defense(board)
    if sq is not None:
        board[sq] = COMPUTER_MARKER
        return

    # center
    if board[5] == INITIAL_MARKER:
        board[5] = COMPUTER_MARKER
        return

    # random
    else:
        square = random.choice(empty_squares(board))
        board[square] = COMPUTER_MARKER

## TT bonus 5. Choose who starts

def choose_who_starts():
    if FIRST_TO_MOVE == 'player':
        return 'player'

    elif FIRST_TO_MOVE == 'computer':
        return 'computer'

    while True:

        prompt('choose 1st move: player or computer:')
        answer = input().strip().lower()

        if answer == 'player' or answer == 'p':
            return 'player'

        elif answer == 'computer' or answer == 'c' or answer == 'comp':
            return 'computer'

        prompt('wrong answer, choose player or computer')

## main function code

def play_tic_tac_toe():
    player_count = 0
    computer_count = 0

    while True: # outer loop to play multiple games
        board = initialize_board()
        current = choose_who_starts()

        # one game
        while True:
            display_board(board)

            if current == 'player':
                player_chooses_square(board)
            else:
                computer_chooses_square(board)

            # check immediately after the move
            if someone_won(board) or board_full(board): # to break loop
                break

            # allows the other one to play
            current = 'computer' if current == 'player' else 'player'

        display_board(board)

        winner = detect_winner(board)

        if someone_won(board):
            prompt(f"{winner} won!")
        else:
            prompt(f"It's a tie!")

    ## TT bonus 2. After inner loop: update and show score

        player_count, computer_count = keep_score(winner, player_count, computer_count)
        prompt(f"First to win {FINAL_WINNER} games is the final winner")
        prompt(f"player wins:{player_count} Computer wins:{computer_count}")

        final_winner = detect_final_winner(player_count, computer_count)
        if final_winner:
            prompt(f"{final_winner} is the final winner!")
            if play_again():
                player_count = 0
                computer_count = 0
                continue #restarts the outer loop without continuing to the end of the loop
            else:
                break

    ## if not final winner yet, this part runs

        if not play_again():
            break

    prompt("Thanks for playing Tic Tac Toe!")

play_tic_tac_toe()

## Flow of play_tic_tact_toe
'''
START
  ↓
Outer loop (whole match)
  ↓
Initialize empty board
  ↓
--------------------------------------
Inner loop (one board = one game)
   ↓
 Player move → check win/tie?
   ↓
 Computer move → check win/tie?
   ↓
 If winner or board full → break inner loop
--------------------------------------
  ↓
Show board + announce result
Update scores
  ↓
Check if FINAL WINNER (5 wins?)
  ├── YES:
  │     ↓
  │   Announce final winner
  │   Ask play_again()
  │      ├── YES: reset scores, continue outer loop (new match)
  │      └── NO: break outer loop (end program)
  │
  └── NO:
        ↓
        Ask play_again()
        ├── YES: continue outer loop (next game, keep scores)
        └── NO: break outer loop (end program)
  ↓
"Thanks for playing!"
END

## KEY TAKEAWAYS

Inner loop = keeps running until a board finishes (win/tie).

Outer loop = keeps running until player decides to quit.

Two play_again checks:

One inside if final_winner: → restart whole match OR quit.

One at bottom → ask if you want to play another game (when no one reached has reached 5 yet).

the second play_again is only reached if there's no final winner.
there is no repetition asking the question twice.
'''