import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(sol.lenLongestFibSubseq(arr), 5)
    
    def test_case_2(self):
        sol = Solution()
        arr = [1, 3, 7, 11, 12, 14, 18]
        self.assertEqual(sol.lenLongestFibSubseq(arr), 3)
