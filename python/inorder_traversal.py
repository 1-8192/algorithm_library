# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:

# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:

# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

# Constraints:

#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100
 
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution
def inorderTraversal_recursive(root):
    result = []
    
    def inorder(node):
        if not node:
            return
        
        # Visit left subtree
        inorder(node.left)
        
        # Visit current node
        result.append(node.val)
        
        # Visit right subtree
        inorder(node.right)
    
    inorder(root)
    return result

# Iterative Solution
def inorderTraversal_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        
        # Current is now None, pop the stack
        current = stack.pop()
        
        # Visit the node
        result.append(current.val)
        
        # Move to the right subtree
        current = current.right
    
    return result

# Helper function to create tree from list representation
def create_tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        node = queue.pop(0)
        
        # Add left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
test_cases = [
    [1, None, 2, 3],
    [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9],
    [],
    [1]
]

for i, case in enumerate(test_cases):
    print(f"Example {i+1}:")
    print(f"Input: {case}")
    
    # Create tree from list
    root = create_tree(case)
    
    # Test recursive solution
    result_recursive = inorderTraversal_recursive(root)
    print(f"Output (recursive): {result_recursive}")
    
    # Test iterative solution
    result_iterative = inorderTraversal_iterative(root)
    print(f"Output (iterative): {result_iterative}")
    print()