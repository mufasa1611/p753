import random
import copy
from termcolor import colored

# Define the Initial Board
Initial_board = [[1, 2, 3, 4, 5, 6, 7],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3]]


# Get Player Name
def get_player_name():
    while True:
        player = input("Enter your name: ").strip()
        if player.isalpha():
            return player
        else:
            print(colored("Invalid input."
                  "Please enter alphabetic characters only.", "red"))


# Display the Initial Board

def display_board(board):
    for i, row in enumerate(board, start=1):
        formatted_row = f"row {i}: " + " " .join(
            [colored('X', 'green') for _ in row])
        print(formatted_row)


# Take Units from a row
def take_units(row, units):
    if units < 1 or units > len(row):
        print(
            f"Invalid input. You can take between 1"
            f"and {len(row)} items. Please Try again.")
        return False

    row[-units:] = []
    return True


# Calculate remaining units on the board
def units_left(board):
    return sum(map(len, board))


# Execute Player Turn
def player_turn(board, player):
    print(colored(f"\n{player}'s ", "blue") + f" Turn:")
    display_board(board)

    # Select a row
    pick_row = None
    selected_row = None
    while pick_row is None or pick_row < 1 or \
            pick_row > 3 or len(board[pick_row - 1]) == 0:

        try:
            pick_row = int(input(colored("Choose a row "
                           "(1, 2, or 3): ", "yellow")))
            if pick_row < 1 or pick_row > 3:
                print(colored("Invalid row choice. "
                      "Please enter 1, 2, or 3.", "red"))
            elif len(board[pick_row - 1]) == 0:
                print(colored("That row is empty. Choose another row.", "red"))
            else:
                selected_row = board[pick_row - 1]
        except ValueError:
            print(colored("Invalid input. "
                  "Please enter a valid number.", "red"))

    # Select units
    units = None
    while units is None or units < 1 or units > len(selected_row) \
            or units >= units_left(board):
        try:
            units = int(input(colored(f"How many units "
                        f"to take from row {pick_row}? ", "yellow")))
            if units is None or units < 1 or units > len(selected_row) \
                    or units >= units_left(board):
                print(colored(
                    "Invalid input. Please enter a number between 1 and "
                    f"{min(len(selected_row),units_left(board) - 1)}.", "red"))
        except ValueError:
            print(colored(
                 "Invalid input. Please enter a valid number.", "red"))

    take_units(selected_row, units)


# Computer turn
def computer_turn(board):
    print(colored("\nComputer's", "magenta") + f" Turn:")

    available_rows = [i for i, row in enumerate(board) if len(row) > 0]
    if not available_rows:
        print(colored("\nComputer wins!", "red"))
        return

    pick_row = random.choice(available_rows)
    selected_row = board[pick_row]
    max_units = min(len(selected_row), units_left(board) - 1)
    units = random.randint(1, max_units)
    take_units(selected_row, units)
    print(colored(
        f"Computer took {units} units from row {pick_row + 1}.", "yellow"))


# Game Loop
def play_game(player):
    current_board = copy.deepcopy(Initial_board)

    while True:
        player_turn(current_board, player)
        display_board(current_board)

        if sum(map(len, current_board)) == 1:
            print(colored(f"\n{player} ", "green") + "wins!")
            break

        computer_turn(current_board)

        if sum(map(len, current_board)) == 1:
            display_board(current_board)
            print(colored("\nComputer", "red") + " wins!")
            break


# Game intro
print(colored("\n Welcome to the (7/5/3) Game of Rows!\n", "cyan"))
print(' In this game, you have three rows of tokens represented by "X".')
print(" Each row has a different number of tokens.")
print(" On your turn, you can choose a row and take "
      "a certain number of tokens from it.")
print(" The goal is to leave the last unit for your opponent.\n")
print(colored(" Let's get started!\n", "cyan"))

# Game start
players = get_player_name()
while True:
    play_game(players)

    # Retry or quit option
    play_again = input(
        f"\nDo you want to play again {players}? (yes/no): ").strip().lower()
    if not play_again.startswith('y'):
        print(colored(f"Goodbye!", "yellow")+colored(f" {players}", "blue"))
        break
