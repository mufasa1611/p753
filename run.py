# Import Required Module 
import random
        
# Define the Initial Board
rows = [[1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5],
        [1, 2, 3]]

#  Get Player Name
def get_player_name():
    while True:
        player_name = input("Enter your name: ").strip()
        if player_name:
            return player_name        
