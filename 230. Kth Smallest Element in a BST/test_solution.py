import unittest
from solution import Solution, TreeNode



class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
        k = 1
        self.assertEqual(sol.kthSmallest(root, k), 1)
    
    def test_case_2(self):
        sol = Solution()
        root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
        k = 3
        self.assertEqual(sol.kthSmallest(root, k), 3)
