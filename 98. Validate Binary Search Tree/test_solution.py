import unittest
from solution import TreeNode, Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(Solution().isValidBST(root))
    
    def test_case_2(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(Solution().isValidBST(root))
    
    def test_case_3(self):
        root = TreeNode(1)
        self.assertTrue(Solution().isValidBST(root))
