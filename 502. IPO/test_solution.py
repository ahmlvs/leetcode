import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]), 4)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]), 6)
