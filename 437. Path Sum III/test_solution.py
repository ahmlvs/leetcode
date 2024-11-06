import unittest
from solution import TreeNode, Solution

# Helper function to create a binary tree from a list (level-order)
def list_to_binary_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

class TestSolution(unittest.TestCase):
    
    def test_case1(self):
        solution = Solution()
        root = list_to_binary_tree([10,5,-3,3,2,None,11,3,-2,None,1])
        targetSum = 8
        self.assertEqual(solution.pathSum(root, targetSum), 3)
    
    def test_case2(self):
        solution = Solution()
        root = list_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
        targetSum = 22
        self.assertEqual(solution.pathSum(root, targetSum), 3)
