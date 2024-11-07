import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    
    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.eraseOverlapIntervals([[1,2],[2,3]]), 0)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.eraseOverlapIntervals([[1, 3], [2, 3], [3, 4], [1, 2]]), 1)
