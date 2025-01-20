"""Lerato Moholo
22 September 2024
util.py
"""

def create_grid(grid):
    """Create a 4x4 array of zeroes within grid"""
    for i in range(4):
        grid.append([0] * 4)  # Appending a list with 4 zeroes for each row

def print_grid(grid):
    """Print out a 4x4 grid in 5-width columns within a box, replacing 0 with an empty space"""
    print("+--------------------+")  # Top border of the box
    for row in grid:
        print("|", end="")  # Left border of the box
        for cell in row:
            if cell == 0:
                print(f"{' ':^5}", end="")  # Replace 0 with an empty space
            else:
                print(f"{cell:^5}", end="")  # Print each cell in a 5-width column, centered
        print("|")  # Right border of the box
    print("+--------------------+")  # Bottom border of the box

def check_lost(grid):
    """Return True if there are no 0 values and no adjacent values that are equal, otherwise False"""
    # Check for any zeroes in the grid
    for row in grid:
        if 0 in row:
            return False  # A zero means the game isn't lost
    
    # Check for adjacent equal values (horizontally and vertically)
    for i in range(4):
        for j in range(4):
            # Check horizontally (right neighbor)
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            
            # Check vertically (bottom neighbor)
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    
    return True  # No zeros and no adjacent equal values, so the game is lost

def check_won(grid):
    """Return True if a value >= 32 is found in the grid; otherwise False"""
    for row in grid:
        for cell in row:
            if cell >= 32:
                return True
    return False

def copy_grid(grid):
    """Return a copy of the given grid"""
    return [row[:] for row in grid]  # Create a deep copy of the grid

def grid_equal(grid1, grid2):
    """Check if two grids are equal - return boolean value"""
    return grid1 == grid2