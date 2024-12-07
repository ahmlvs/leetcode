import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLIS([x for x in range(-1, -10000000, -1)]), 1)
