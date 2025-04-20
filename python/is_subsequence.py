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
    
    # Test with the examples
    print(isSubsequence("abc", "ahbgdc"))  # Expected: True
    print(isSubsequence("axc", "ahbgdc"))  # Expected: False

    # More complex approach to handle array of strings to check.
    def preprocessString(t: str) -> dict:
        """
        Preprocess string t by creating a dictionary that maps each character
        to an array of its positions in the string.
    
        Args:
            t: The source string
    
        Returns:
            A dictionary where keys are characters and values are lists of positions
        """
        char_indices = {}
        for i, char in enumerate(t):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)
        return char_indices

    def isSubsequenceOptimized(s: str, char_indices: dict) -> bool:
        """
        Check if string s is a subsequence using preprocessed character indices.
    
        Args:
            s: The potential subsequence string
            char_indices: The preprocessed dictionary mapping characters to their positions
    
        Returns:
            True if s is a subsequence, False otherwise
        """
        if not s:
            return True
    
        curr_pos = -1  # Current position in t
    
        for char in s:
            # If character doesn't exist in t, s cannot be a subsequence
            if char not in char_indices:
                return False
        
            # Find the next position of this character that's after curr_pos
            indices = char_indices[char]
            idx = binary_search(indices, curr_pos)
        
            # If no valid position found, s cannot be a subsequence
            if idx == len(indices):
                return False
        
            # Update current position to this found position
            curr_pos = indices[idx]
    
        return True

    def binary_search(arr, target):
        """
        Binary search to find the first position in arr that is > target
    
        Args:
            arr: Sorted array of indices
            target: The position to search for
    
        Returns:
            The index of the first element > target, or len(arr) if none exists
        """
        left, right = 0, len(arr)
    
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
    
        return left

    # Example usage for the follow-up scenario 
    def checkManySubsequences(t: str, subsequences: list) -> list:
        """
        Check multiple strings against the same target string t
    
        Args:
            t: The source string
            subsequences: List of strings to check
    
        Returns:
            List of booleans indicating if each string is a subsequence
        """
        char_indices = preprocessString(t)
        results = []
    
        for s in subsequences:
            results.append(isSubsequenceOptimized(s, char_indices))
    
        return results

    # Example
    t = "ahbgdc"
    subsequences = ["abc", "axc", "ahbgdc", ""]
    results = checkManySubsequences(t, subsequences)
    print(results)  # Expected: [True, False, True, True]
