import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        x = 1
        y = 4
        expected = 2
        solution = Solution()
        self.assertEqual(solution.hammingDistance(x, y), expected)
    
    def test_case_2(self):
        x = 3
        y = 1
        expected = 1
        solution = Solution()
        self.assertEqual(solution.hammingDistance(x, y), expected)
