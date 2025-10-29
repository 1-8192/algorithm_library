# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

#     For examples, if arr = [2,3,4], the median is 3.
#     For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.

# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Slow solution O(nklog(k))
        """
        medians = []
        i = 0
        while i <= (len(nums) - k):
            sub_array = nums[i:i+k]
            sub_array.sort()
            if k % 2 == 0:
                index = k // 2 - 1
                index_two = k // 2
                medians.append((sub_array[index_two] + sub_array[index]) / 2)
            else:
                index = k // 2
                medians.append(sub_array[index])
            i = i + 1
        
        return medians
    
    def medianSlidingWindowHeap(self, nums: List[int], k: int) -> List[float]:
        