# Human vs Human Tic-Tac-Toe 
import time

# Initialize board
board = [" " for _ in range(9)]

# Function to print the current board
def print_board():
    print("\nCurrent Board:")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Function to check for a winner
def check_winner(b, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in win_combos)

# Function to check for a tie
def is_tie():
    return " " not in board

# Function to handle a player's move
def player_move(player):
    valid = False
    while not valid:
        move = input(f"{player}'s turn (0-8): ")
        if move.isdigit() and int(move) in range(9):
            move = int(move)
            if board[move] == " ":
                board[move] = player
                valid = True
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid input. Enter a number between 0 and 8.")

# Main game function
def play_game():
    print("Welcome to Tic-Tac-Toe (Human vs Human)!")
    print("Positions are numbered 0 to 8 like this:")
    print("| 0 | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |\n")
    current_player = "X"
    print_board()

    while True:
        player_move(current_player)
        print_board()
        
        if check_winner(board, current_player):
            print(f"🎉 {current_player} wins the game!")
            break
        elif is_tie():
            print("It's a tie!")
            break
        else:
            current_player = "O" if current_player == "X" else "X"
        time.sleep(0.5)

if __name__ == "__main__":
    play_game()
