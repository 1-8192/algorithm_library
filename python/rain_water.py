# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

 

# Constraints:

#     n == height.length
#     1 <= n <= 2 * 104
#     0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        High-Level Algorithm Steps:

        Initialize left and right pointers
        Initialize left_max and right_max variables
        Initialize total trapped water to zero
        While left pointer is less than right pointer:

        Compare max heights from left and right
        Move the pointer with smaller max height
        Calculate and add trapped water at the current position

        Return total trapped water
        '''
        total_rain = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_rain += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_rain += right_max - height[right]
                right -= 1

        return total_rain