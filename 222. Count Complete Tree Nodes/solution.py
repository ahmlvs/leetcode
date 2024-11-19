# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # func to calc depth for leftmost and rightmost
        def get_depth(node, left=True):
            depth = 0
            while node:
                # to next level
                node = node.left if left else node.right
                depth += 1
            
            return depth
        
        left_depth = get_depth(root, True)
        right_depth = get_depth(root, False)

        # if left_depth == right_depth
        # it means that tree is fully complete
        # so number of the nodes is 2**depth - 1
        if left_depth == right_depth:
            return 2**left_depth - 1
        # if not we need to recalculate for left and right subtree
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        # efficient log(n) for depth
        # and log(n) for repeat
        # so log^2(n)
