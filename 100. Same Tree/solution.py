# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def in_order_traversal(node, values):
        #     if not node:
        #         values.append(None)
        #         return
            
        #     values.append(node.val)
        #     in_order_traversal(node.left, values)
        #     in_order_traversal(node.right, values)
        
        # p_values = []
        # in_order_traversal(p, p_values)

        # q_values = []
        # in_order_traversal(q, q_values)

        # return p_values == q_values

        ## recursively

        # if both none
        if not p and not q:
            return True
        
        # if on none
        if not p or not q:
            return False
        
        # check values
        if p.val != q.val:
            return False
        
        # if both ok return recursively for left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
