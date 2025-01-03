# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example 1:


# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
 

# Follow-up:

# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# find next available node on level
def find_next(node):
    while node:
        if node.left:
            return node.left
        if node.right:
            return node.right
        node = node.next
    return None

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # we are on root
        # and for childs
        # exp1. on 2
        # 4->5
        if root.left:
            root.left.next = root.right if root.right else find_next(root.next)
        
        # exp1. on 2
        # 5->7, because 2.next -> 3
        if root.right:
            root.right.next = find_next(root.next)
        
        # rec for left and right subs
        # first right, because we need right links
        self.connect(root.right)
        self.connect(root.left)

        return root
