import random

# Getting the player names
first_player = input('Choose alias name:\n')
second_player = input('Choose alias name:\n')
player = [first_player, second_player]

print(f'*********TIC-TAC-TOE GAME COMPETITION BETWEEN {first_player} Vs {second_player} *******\n')

# Random selection of the player to start the first move and fair play
starter = random.choice(player)
other_player = player[1] if starter == player[0] else player[0]
print(f"Lets see who starts first: {starter}\n")

# Initialize the Tic-Tac-Toe board
tic_tac_toe_board = [[' '] * 3 for _ in range(3)]


# Function to print the current state of the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


# Function to check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None


# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


# Main game function
def tic_tac_toe_game():
    current_player = starter
    symbol = 'X' if current_player == starter else 'O'

    while True:
        print_board(tic_tac_toe_board)

        # Get the current player's move
        try:
            row = int(input(f'{current_player}: Choose row (0-2): '))
            col = int(input(f'{current_player}: Choose column (0-2): '))

            # Ensure the move is within bounds and the cell is not already taken
            if row < 0 or row > 2 or col < 0 or col > 2 or tic_tac_toe_board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Place the player's symbol on the board
        tic_tac_toe_board[row][col] = symbol

        # Check for a winner after the move
        winner = check_winner(tic_tac_toe_board)
        if winner:
            print_board(tic_tac_toe_board)
            print(f"Congratulations! {current_player} wins!")
            break

        # Check for a draw
        if is_board_full(tic_tac_toe_board):
            print_board(tic_tac_toe_board)
            print("It's a draw!")
            break

        # Switch players
        current_player = other_player if current_player == starter else starter
        symbol = 'O' if symbol == 'X' else 'X'


# Start the gamesss
tic_tac_toe_game()
