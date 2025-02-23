import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.maxSum([[1,2],[3,4]], [1,2], 2), 7)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.maxSum([[5,3,7],[8,2,6]], [2,2], 3), 21)
