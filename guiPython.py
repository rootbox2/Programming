import random

# Constants
PLAYER = "P"
OBSTACLE = "O"
EMPTY = " "

# Game Configuration
GRID_WIDTH = 10
PLAYER_START_POS = 0
OBSTACLE_FREQUENCY = 0.3

def generate_grid(player_pos):
    grid = [EMPTY] * GRID_WIDTH
    grid[player_pos] = PLAYER
    for i in range(GRID_WIDTH):
        if i != player_pos and random.random() < OBSTACLE_FREQUENCY:
            grid[i] = OBSTACLE
    return grid

def display_grid(grid):
    print("".join(grid))

def move_player(grid, direction):
    player_pos = grid.index(PLAYER)
    new_pos = player_pos + direction
    if 0 <= new_pos < GRID_WIDTH:
        grid[player_pos], grid[new_pos] = EMPTY, PLAYER
    return grid

if __name__ == "__main__":
    player_pos = PLAYER_START_POS

    while True:
        grid = generate_grid(player_pos)
        display_grid(grid)

        move = input("Enter 'l' to move left, 'r' to move right, or 'q' to quit: ")
        if move == 'l':
            player_pos = max(0, player_pos - 1)
        elif move == 'r':
            player_pos = min(GRID_WIDTH - 1, player_pos + 1)
        elif move == 'q':
            break
        else:
            print("Invalid input. Try again.")
