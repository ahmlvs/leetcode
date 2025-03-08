import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        self.assertEqual(solution.minimumRecolors("WBBWWBBWBW", 7), 3)
    
    def test_case_2(self):
        solution = Solution()
        self.assertEqual(solution.minimumRecolors("WBWBBBW", 2), 0)
