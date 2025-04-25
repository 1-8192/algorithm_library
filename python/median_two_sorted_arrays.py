# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:

#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays.
        The function first checks if either of the arrays is empty.
        If both are empty, it returns 0.0.
        If one of the arrays is empty, it returns the median of the other array.
        If both arrays are non-empty, it merges them into a single sorted array
        and calculates the median based on the length of the merged array.
        The median is calculated as follows:
        - If the length of the merged array is even, the median is the average of the two middle elements.
        - If the length is odd, the median is the middle element.
        """
        
        if not nums1 and not nums2:
            return 0.0

        merge = self.merge_arrays(nums1, nums2)

        if len(merge) % 2 == 0:
            return (merge[math.floor(len(merge)/2)] + merge[math.floor(len(merge)/2) - 1]) / 2
        else:
            return merge[math.ceil(len(merge)/2) - 1]

    def merge_arrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Merges two sorted arrays into one sorted array using a two-pointer technique. 
        Runtime complexity is O(m+n) where m and n are the lengths of the two arrays.
        """
        merged = []
        i = j = 0

        if not nums1:
            return nums2
        if not nums2:
            return nums1

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
    
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
    
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
    
        return merged
