# Import Required Module 
import random
        
# Define the Initial Board
rows = [[1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5],
        [1, 2, 3]]

#  Get Player Name
def get_player_name():
    while True:
        player = input("Enter your name: ").strip()
        if player:
            return player      

# Display the Initial Board
def display_board(board):
    for i, row in enumerate(board, start=1):
         formatted_row = f"row {i}: " + " ".join([str(unit) for unit in row])
         print(formatted_row)

# Take Units from a row
def take_units(row, units):
    if units < 1 or units > len(row):
        print(f"Invalid input. You can take between 1 and {len(row)} items. Please Try again.")
        return False

    row[-units:] = []
    return True
    
# Execute Player Turn    
def player_turn(board, player):
    print(f"\n{player}'s Turn:")
    display_board(board)

# Select a row
    selected_row = None
    while selected_row is None or selected_row < 1 or selected_row > 3 or len(board[selected_row - 1]) == 0:
        selected_row = int(input("Choose a row (1, 2, or 3): "))
        if selected_row < 1 or selected_row > 3:
            print("Invalid row choice. Please enter 1, 2, or 3.")
        elif len(board[selected_row - 1]) == 0:
            print("That row is empty. Choose another row.")
    selected_row = board[selected_row - 1]

# Select units
    units = None
    while units is None or units < 1 or units > len(selected_row):
        units = int(input(f"How many units to take from row {selected_row}? "))
        if units < 1 or units > len(selected_row):
            print(f"Invalid input. Please enter a number between 1 and {len(selected_row)}.")

    take_units(selected_row, units)
