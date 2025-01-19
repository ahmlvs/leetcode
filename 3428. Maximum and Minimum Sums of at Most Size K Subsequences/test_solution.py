import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.minMaxSums([1,2,3], 2), 24)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.minMaxSums([5,0,6], 1), 22)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.minMaxSums([1,1,1], 2), 12)
