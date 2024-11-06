# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # result = []

        # while root:
        #     result.append(root.val)
        #     root = root.right
        
        # return result

        ## need to find right node in each level

        if not root:
            return []
    
        queue = deque()
        queue.append(root)
        right_view = []

        while queue:
            # len of level
            level_lenght = len(queue)

            for i in range(level_lenght):
                node = queue.popleft()

                # only right element to right_view
                if i == level_lenght - 1:
                    right_view.append(node.val)
                
                # add next level nodes to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view
        