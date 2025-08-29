# Given a string s, find the length of the longest

# without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.


def lengthOfLongestSubstring(s):
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of longest substring without repeating characters
    """
    if not s:
        return 0
    
    char_index = {}  # Dictionary to store character and its latest index
    left = 0  # Left pointer of sliding window
    max_length = 0  # Maximum length found so far
    
    for right in range(len(s)):
        char = s[right]
        
        # If character is already in current window, move left pointer
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        # Update character's latest index
        char_index[char] = right
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Alternative solution using set (slightly different approach)
def lengthOfLongestSubstring_set(s):
    """
    Alternative solution using a set to track characters in current window.
    """
    if not s:
        return 0
    
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test with provided examples
def test_solution():
    test_cases = [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),     # "b"
        ("pwwkew", 3),    # "wke"
        ("", 0),          # empty string
        ("dvdf", 3),      # "vdf"
        ("abcdef", 6),    # entire string
        ("a", 1),         # single character
    ]
    
    print("Testing lengthOfLongestSubstring:")
    for s, expected in test_cases:
        result = lengthOfLongestSubstring(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' → Output: {result} (Expected: {expected})")
    
    print("\nTesting alternative solution:")
    for s, expected in test_cases:
        result = lengthOfLongestSubstring_set(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' → Output: {result} (Expected: {expected})")


if __name__ == "__main__":
    test_solution()