"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Ngoc Khanh Vy Tranová
email: ngtranova@gmail.com
discord: veelilly 
"""
import random

# Main game

def game():

    # introduction
    game_rules = """GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their 
    marks in a: 
    * horizontal,
    * vertical or
    * diagonal row"""

    board =[" ", " ", " ", " ", " ", " ", " ", " ", " "]
    separator = "=" * 40

    print(separator)
    player = input("Hey there! How should I call you?: ")
    print(separator)
    print(f"Hello {player}. Welcome to Tic Tac Toe!")
    print(separator)
    print(game_rules)
    print(separator)
    print("Let's start the game!")
    print(separator)

    # player chooses X or O, the other is the computer
    player_mark = player_mark_choice()
    computer_mark = "O" if player_mark == "X" else "X"

    # random choice of first turn
    turn = starting_player()
    if turn == "player":
        print(f"{player_mark} goes first!")
    else:
        print(f"{computer_mark} goes first!")

    # display the gameboard
    display_the_gameboard(board)
    print(separator)

    # game loop
    while True:
        if turn == "player":
            move = player_move(board)
            board[move] = player_mark
            display_the_gameboard(board)

            # player win check 
            if check_win(board, player_mark):
                print(f"Congratulation {player}, you WON!")
                break
            turn = "computer"
        else: 
            move = computer_move(board)
            board[move] = computer_mark
            display_the_gameboard(board)

            # computer win check
            if check_win(board, computer_mark):
                print("Oh, you lost!")
                break
            turn = "player"

        # draw check
        if check_draw(board):
            print("It's a draw!")
            break
        print(separator)

# function for player to choose their mark
def player_mark_choice():
    while True:
        mark_choice = input("Would you like to play 'X' or 'O'?: ").upper()
        if mark_choice in ["X", "O"]:
            print(f"You will be playing {mark_choice}!")
            return mark_choice
        else:
            print("That's not an option. Please select 'X' or 'O'!")

# function to randomly choose the starting player
def starting_player():
    return random.choice(["player", "computer"])

# function to display the gameboard
def display_the_gameboard(board):
    print("+---+---+---+")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("+---+---+---+")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("+---+---+---+")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("+---+---+---+")

# function for player's move
def player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if move in range (0,9): 
                if board[move] == " ":
                    return move
                # if the space is taken
                else:
                    print("That space is taken! Please try again!") 
            # The input is outside the board
            else:
                print(f"{move} not in board! Please enter a number between 1 and 9: ")
        # invalid input (not a number)   
        else:
            print("That's not a number. Please try again!")

# function for computer's move
def computer_move(board):
    possible_moves = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(possible_moves)

# function to check for a win
def check_win(board, mark):
    win_combination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],    # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],    # vertical
        [0, 4, 8], [2, 4, 6]                # diagonal
    ]
    for combination in win_combination:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == mark:
            return True
    return False

# function to chech for a draw
def check_draw(board):
    return " " not in board
        
# game entry        
if __name__ == "__main__":
    game()