# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example 1:

# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:

# Input: grid = [[1]]
# Output: 4

# Example 3:

# Input: grid = [[1,0]]
# Output: 4

# Constraints:

#     row == grid.length
#     col == grid[i].length
#     1 <= row, col <= 100
#     grid[i][j] is 0 or 1.
#     There is exactly one island in grid.

def islandPerimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            # If current cell is land
            if grid[i][j] == 1:
                # Start with 4 sides for this land cell
                sides = 4
                
                # Check all four adjacent cells and subtract for shared edges
                # Check cell above
                if i > 0 and grid[i-1][j] == 1:
                    sides -= 1
                
                # Check cell below
                if i < rows-1 and grid[i+1][j] == 1:
                    sides -= 1
                
                # Check cell to the left
                if j > 0 and grid[i][j-1] == 1:
                    sides -= 1
                
                # Check cell to the right
                if j < cols-1 and grid[i][j+1] == 1:
                    sides -= 1
                
                # Add the remaining sides to the perimeter
                perimeter += sides
    
    return perimeter

# Test with examples
example1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(f"Example 1: {islandPerimeter(example1)}")  # Expected: 16

example2 = [[1]]
print(f"Example 2: {islandPerimeter(example2)}")  # Expected: 4

example3 = [[1,0]]
print(f"Example 3: {islandPerimeter(example3)}")  # Expected: 4

