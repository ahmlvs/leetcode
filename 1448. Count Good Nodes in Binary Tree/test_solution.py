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
        root = list_to_binary_tree([3,1,4,3,None,1,5])
        self.assertEqual(solution.goodNodes(root), 4)
    
    def test_case2(self):
        solution = Solution()
        root = list_to_binary_tree([3,3,None,4,2])
        self.assertEqual(solution.goodNodes(root), 3)
    
    def test_case3(self):
        solution = Solution()
        root = list_to_binary_tree([1])
        self.assertEqual(solution.goodNodes(root), 1)
