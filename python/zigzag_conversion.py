# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 
# Constraints:
#     1 <= s.length <= 1000
#     s consists of English letters (lower-case and upper-case), ',' and '.'.
#     1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert string to zigzag pattern and read line by line.
    
        Args:
            s: Input string
            numRows: Number of rows in zigzag pattern
    
        Returns:
            String read line by line from zigzag pattern
        """
        # Edge case: if numRows is 1, no zigzag needed
        if numRows == 1:
            return s
    
        # Create list of strings for each row
        rows = [''] * numRows
    
        # Track current row and direction
        current_row = 0
        going_down = True
    
        # Place each character in appropriate row
        for char in s:
            rows[current_row] += char
        
            # Change direction at top and bottom
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
        
            # Move to next row
            if going_down:
                current_row += 1
            else:
                current_row -= 1
    
        # Concatenate all rows
        return ''.join(rows)