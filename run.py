# Import Required Module
import random
import copy

# Define the Initial Board
Initial_board = [[1, 2, 3, 4, 5, 6, 7],
                 [1, 2, 3, 4, 5],
                 [1, 2, 3]]

#  Get Player Name
def get_player_name():
    while True:
        player = input("Enter your name: ").strip()
        if player.isalpha():
            return player
        else:
            print("Invalid input. Please enter alphabetic characters only.")

# Display the Initial Board
def display_board(board):
    for i, row in enumerate(board, start=1):
        formatted_row = f"row {i}: " + " ".join([str(unit) for unit in row])
        print(formatted_row)

# Take Units from a row
def take_units(row, units):
    if units < 1 or units > len(row):
        print(
            f"Invalid input. You can take between 1",
            f"and {len(row)} items. Please Try again."
        )
        return False

    row[-units:] = []
    return True

# Execute Player Turn
def player_turn(board, player):
    print(f"\n{player}'s Turn:")
    display_board(board)

    # Select a row
    pick_row = None
    selected_row = None
    while pick_row is None or pick_row < 1 or \
            pick_row > 3 or len(board[pick_row - 1]) == 0:

            try:
                pick_row = int(input("Choose a row (1, 2, or 3): "))
                if pick_row < 1 or pick_row > 3:
                    print("Invalid row choice. Please enter 1, 2, or 3.")
                elif len(board[pick_row - 1]) == 0:
                    print("That row is empty. Choose another row.")
                else:
                    selected_row = board[pick_row - 1]
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Select units
    units = None
    while units is None or units < 1 or units > len(selected_row):
        try:
            units = int(input(f"How many units to take from row {pick_row}? "))
            if units < 1 or units > len(selected_row):
                print(
                    f"Invalid input. Please enter a number",
                   f" between 1 and {len(selected_row)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    take_units(selected_row, units)

    # Computer turn
def computer_turn(board):
    print("\nComputer's Turn:")

    available_rows = [i for i, row in enumerate(board) if len(row) > 0]
    if not available_rows:
        print("Computer wins!")
        return

    pick_row = random.choice(available_rows)
    selected_row = board[pick_row]
    units = random.randint(1, len(selected_row))
    take_units(selected_row, units)
    print(f"Computer took {units} units from row {pick_row + 1}.")

# Game Loop
def play_game(player):
    current_board = copy.deepcopy(Initial_board)

    while True:
        player_turn(current_board, player)
        display_board(current_board)

        if sum(map(len, current_board)) == 1:
            print(f"{player} wins!")
            break

        computer_turn(current_board)

        if sum(map(len, current_board)) == 1:
            display_board(current_board)
            print("Computer wins!")
            break


# Game intro
print("\nWelcome to the Game of Rows!")
print("In this game, you have three rows of tokens (represented by numbers).")
print("Each row has a different number of tokens.")
print("On your turn, you can choose a row and \
take a certain number of tokens from it.")
print("The goal is to leave the last unit for your opponent.\n")
print("Let's get started!\n")

# Game start
player = get_player_name()
while True:
    play_game(player)

# Retry or quit option
    play_again = input(
        f"Do you want to play again {player}? (yes/no): ").strip().lower()
    if not play_again.startswith('y'):
        print(f"Goodbye! {player}")
        break
