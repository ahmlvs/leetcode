# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105
 

# Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order_traversal(node, values):
            if not node:
                return
            
            ## get values in asc order
            # add values for left subtrees
            in_order_traversal(node.left, values)
            # add node value
            values.append(node.val)
            # add values for right subtrees
            in_order_traversal(node.right, values)
        
        values = []
        in_order_traversal(root, values)
        
        # biggest number for start
        total_min_diff = float('inf')
        
        # for asc order simply check one by one
        for i in range(1,len(values)):
            total_min_diff = min(total_min_diff, values[i] - values[i-1])
        
        return total_min_diff
        