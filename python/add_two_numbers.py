# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#         It is guaranteed that the list represents a number that does not have leading zeros.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# HELPER FUNCTIONS FOR TESTING
def create_linked_list(digits):
    """Create a linked list from a list of digits"""
    if not digits:
        return None
    
    head = ListNode(digits[0])
    current = head
    for digit in digits[1:]:
        current.next = ListNode(digit)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert linked list back to Python list for easy viewing"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# TEST THE SOLUTIONS
if __name__ == "__main__":
    # Test case 1: [2,4,3] + [5,6,4] = [7,0,8] (342 + 465 = 807)
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    
    solution1 = Solution()
    result1 = solution1.addTwoNumbers(l1, l2)
    print(f"Test 1 - Improved Solution 1: {linked_list_to_list(result1)}")
    
    # Recreate lists for second test (since they were modified)
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    
    solution2 = Solution()
    result2 = solution2.addTwoNumbers(l1, l2)
    print(f"Test 1 - Improved Solution 2: {linked_list_to_list(result2)}")
    
    # Test case 2: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([9,9,9,9])
    
    solution1 = Solution()
    result1 = solution1.addTwoNumbers(l1, l2)
    print(f"Test 2 - Improved Solution 1: {linked_list_to_list(result1)}")

"""
ANALYSIS OF ORIGINAL SOLUTION:

ISSUES:
1. **Inefficiency**: Converts entire numbers to strings/integers
   - Time: O(max(m,n)) for traversal + O(max(m,n)) for string operations
   - Space: O(max(m,n)) for string storage + O(max(m,n)) for result
   
2. **Potential Overflow**: Large numbers may exceed integer limits
   - Example: 100-digit numbers would cause integer overflow
   
3. **Unnecessary String Operations**: Multiple string reversals and conversions
   - Converting digits to strings, reversing, converting back to int
   - Then converting result to string and reversing again
   
4. **Complex Result Construction**: Manual loop with index checking
   - The final loop is more complex than needed
   - Creates next node inside the loop with look-ahead logic

IMPROVEMENTS IN NEW SOLUTIONS:

1. **Direct Digit Processing**: Process one digit at a time
   - No string conversions or integer arithmetic on large numbers
   - Handles arbitrarily large numbers without overflow
   
2. **Carry Handling**: Proper carry propagation digit by digit
   - More intuitive and matches manual addition process
   
3. **Cleaner Code Structure**: 
   - Single loop handles all cases
   - Dummy head simplifies list construction
   - No complex indexing or look-ahead logic
   
4. **Better Space Complexity**: Only stores result, no intermediate strings
   
5. **Edge Case Handling**: Naturally handles different length lists and final carry

TIME COMPLEXITY: O(max(m, n)) where m, n are lengths of input lists
SPACE COMPLEXITY: O(max(m, n)) for the result list only

The improved solutions are more efficient, readable, and handle edge cases better.
"""

