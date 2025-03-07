import numpy as np

# Create an empty 32x32 grid
grid = np.zeros((32, 32), dtype=int)

# Define walls (1s) surrounding the grid and rooms
grid[:, [0, -1]] = 1  # Left and right walls
grid[[0, -1], :] = 1  # Top and bottom walls

# Create four locked rooms with 1s as walls
grid[8:24, 8] = 1  # Vertical wall left
grid[8:24, 24] = 1  # Vertical wall right
grid[8, 8:24] = 1  # Horizontal top wall
grid[24, 8:24] = 1  # Horizontal bottom wall

# Doors (use 2 for doors)
grid[10, 8] = 2  # Door to first room
grid[10, 24] = 2  # Door to second room
grid[22, 8] = 2  # Door to third room
grid[22, 24] = 2  # Door to final room

# Keys (use 3 for keys)
grid[6, 6] = 3  # First key (outside)
grid[12, 10] = 3  # Second key (inside first room)
grid[12, 22] = 3  # Third key (inside second room)
grid[20, 10] = 3  # Fourth key (inside third room)
grid[20, 22] = 3  # Chip inside the final room

# Flatten the grid into a 1024-element array
upper_layer = grid.flatten().tolist()

print(upper_layer)  # This will print the full 1024-element array
