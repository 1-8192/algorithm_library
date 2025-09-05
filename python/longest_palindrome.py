# Given a string s, return the longest palindromic substring
# in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters.

def longest_palindrome_expand_around_centers(s):
    """
    Approach 1: Expand Around Centers
    Time: O(n²), Space: O(1)
    
    For each possible center, expand outward while characters match.
    Handle both odd-length (single center) and even-length (two centers) palindromes.
    """
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Check for odd-length palindromes (center at i)
        len1 = expand_around_center(i, i)
        # Check for even-length palindromes (center between i and i+1)
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]


def longest_palindrome_dp(s):
    """
    Approach 2: Dynamic Programming
    Time: O(n²), Space: O(n²)
    
    Build a 2D table where dp[i][j] represents whether substring s[i:j+1] is palindrome.
    """
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for 2-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]


def longest_palindrome_manacher(s):
    """
    Approach 3: Manacher's Algorithm (Advanced)
    Time: O(n), Space: O(n)
    
    Most efficient algorithm for this problem.
    Preprocesses string and uses previously computed information.
    """
    if not s:
        return ""
    
    # Preprocess: insert '#' between characters
    # "babad" -> "#b#a#b#a#d#"
    processed = '#'.join('^{}$'.format(s))
    n = len(processed)
    P = [0] * n  # P[i] = length of palindrome centered at i
    center = right = 0
    
    for i in range(1, n - 1):
        mirror = 2 * center - i
        
        if i < right:
            P[i] = min(right - i, P[mirror])
        
        # Try to expand palindrome centered at i
        try:
            while processed[i + (1 + P[i])] == processed[i - (1 + P[i])]:
                P[i] += 1
        except IndexError:
            pass
        
        # If palindrome centered at i extends past right, adjust center and right
        if i + P[i] > right:
            center, right = i, i + P[i]
    
    # Find the longest palindrome
    max_len = max(P)
    center_index = P.index(max_len)
    start = (center_index - max_len) // 2
    
    return s[start:start + max_len]


# Test the solutions
def test_solutions():
    test_cases = [
        "babad",
        "cbbd", 
        "a",
        "ac",
        "racecar",
        "noon",
        "abcdef"
    ]
    
    solutions = [
        ("Expand Around Centers", longest_palindrome_expand_around_centers),
        ("Dynamic Programming", longest_palindrome_dp),
        ("Manacher's Algorithm", longest_palindrome_manacher)
    ]
    
    for test in test_cases:
        print(f"\nInput: '{test}'")
        for name, func in solutions:
            result = func(test)
            print(f"{name}: '{result}'")


if __name__ == "__main__":
    test_solutions()