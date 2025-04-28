# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:

# Input: n = 2
# Output: false

# Constraints:

#     1 <= n <= 231 - 1

def isHappy(n: int) -> bool:
    """
    Determine if a number is happy.
    
    A happy number is one where repeatedly replacing the number with the sum
    of the squares of its digits eventually leads to 1.
    
    Args:
        n: A positive integer
    
    Returns:
        bool: True if n is a happy number, False otherwise
    """
    # Function to calculate sum of squares of digits
    def get_sum_of_squares(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    # We'll use a set to detect cycles
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_sum_of_squares(n)
    
    # If we reached 1, it's a happy number
    return n == 1

# Test cases
print(isHappy(19))  # Expected: True
print(isHappy(2))   # Expected: False