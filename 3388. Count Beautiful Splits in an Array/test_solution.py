import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1,1,2,1]
        self.assertEqual(sol.beautifulSplits(nums), 2)
    
    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3, 4]
        self.assertEqual(sol.beautifulSplits(nums), 0)
    
    def test_case_3(self):
        sol = Solution()
        nums = [1]
        self.assertEqual(sol.beautifulSplits(nums), 0)
    
    def test_case_4(self):
        sol = Solution()
        nums = [1, 1]
        self.assertEqual(sol.beautifulSplits(nums), 0)
    
    def test_case_5(self):
        sol = Solution()
        nums = [1, 1, 1]
        self.assertEqual(sol.beautifulSplits(nums), 1)
