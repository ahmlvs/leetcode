# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105
 

# Follow up: Could you solve it with time complexity O(height of tree)?

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        if root.val > val:
            # search in left subtree
            return self.searchBST(root.left, val)
        
        # else in right subtree
        return self.searchBST(root.right, val)
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # key_node = self.searchBST(root, key)

        # if not key_node:
        #     return root  # no change if key not found
        
        # # if key_node is a leaf node
        # if not key_node.left and not key_node.right:
        #     if root == key_node:
        #         return None
        #     else:
        #         return root
        
        # if not key_node.left and key_node.right:
        #     key_node.val = key_node.right.val
        #     key_node.left = key_node.right.left
        #     key_node.right = key_node.right.right
        # elif not key_node.right and key_node.left:
        #     key_node.val = key_node.left.val
        #     key_node.left = key_node.left.left
        #     key_node.right = key_node.left.right
        # else: # key_node has both subtrees
        #     # find min in right subtree
        #     parent = key_node
        #     node = key_node.right
        #     while node.left:
        #         parent = node
        #         node = node.left
            
        #     key_node.val = node.val

        #     # delete this min node
        #     if parent.left == node:
        #         # connect right subtree of deleted
        #         parent.left = node.right
        #     else:
        #         # it is for logic like 5 - 6 - 8
        #         # we delete 5
        #         # 6 is min node
        #         parent.right = node.right
        
        # return root

        if not root:
            return None
        
        # scan tree to find node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # node found, handle the deletion
            if not root.left and not root.right:  # leaf node
                return None
            elif not root.left:  # only right child
                return root.right
            elif not root.right:  # only left child
                return root.left
            else:  # two children
                # Find minimum node in right subtree
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        
        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
