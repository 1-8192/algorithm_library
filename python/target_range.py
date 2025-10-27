# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

# Constraints:

#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     nums is a non-decreasing array.
#     -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Binary search to reach O(log N) time complexity
        """

        if not nums:
            return [-1, -1]
        
        left_pos = self.findLeft(nums, target)

        if left_pos == -1:
            return [-1, -1]

        right_pos = self.findRight(nums, target)

        if right_pos == -1:
            return [left_pos, left_pos]
        
        return [left_pos, right_pos]
    
    def findLeft(self, nums, target):
        result = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    
    def findRight(self, nums, target):
        result = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result