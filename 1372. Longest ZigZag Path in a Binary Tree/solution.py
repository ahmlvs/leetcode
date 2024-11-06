# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

 

# Example 1:


# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# Example 2:


# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
# Example 3:

# Input: root = [1]
# Output: 0
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5 * 104].
# 1 <= Node.val <= 100

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # def maxZigZag(node, direction):
        #     if not node:
        #         return 0
            
        #     max_zig_zag = 0

        #     while node:
        #         if direction == 'right':
        #             # check right
        #             if node.right:
        #                 max_zig_zag += 1

        #             node = node.right
        #             direction = "left"
        #         else:
        #             # check left
        #             if node.left:
        #                 max_zig_zag += 1

        #             node = node.left
        #             direction = "right"

        #     return max_zig_zag
        
        # longest_zig_zag = 0
        # stack = deque()
        # stack.append(root)

        # while stack:
        #     node = stack.popleft()
        #     left = maxZigZag(node, "left")
        #     right = maxZigZag(node, "right")

        #     longest_zig_zag = max(longest_zig_zag, left, right)

        #     if node.left:
        #         stack.append(node.left)
            
        #     if node.right:
        #         stack.append(node.right)

        # return longest_zig_zag

        self.max_length = 0

        def dfs(node, direction, lenght):
            if not node:
                # no max_length update
                return
            
            # update max_length
            self.max_length = max(self.max_length, lenght)

            if direction == "left":
                # continue zigzag to left
                dfs(node.left, "right", lenght+1)
                # reset length and switch to right
                dfs(node.right, "left", 1)
            else: # direction == "right"
                dfs(node.right, "left", lenght+1)
                dfs(node.left, "right", 1)

        
        dfs(root.left, "right", 1)
        dfs(root.right, "left", 1)

        return self.max_length
        