# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:

#     0 <= s.length <= 100
#     0 <= t.length <= 104
#     s and t consist only of lowercase English letters.
 
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Check if string s is a subsequence of string t.
    
        Args:
            s: The potential subsequence string
            t: The source string
    
        Returns:
            True if s is a subsequence of t, False otherwise
        """
        if not s:  # Empty string is always a subsequence
            return True
    
        if not t:  # If s is not empty but t is, s cannot be a subsequence
            return False
    
        i = 0  # Pointer for string s
    
        # Iterate through string t
        for char in t:
            # If we find a matching character, move the pointer in s
            if i < len(s) and char == s[i]:
                i += 1
        
            # If we've matched all characters in s, return True
            if i == len(s):
                return True
    
        # If we've gone through all of t and haven't matched all of s
        return i == len(s)