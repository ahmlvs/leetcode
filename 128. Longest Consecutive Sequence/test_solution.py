import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.longestConsecutive([100,4,200,1,3,2]), 4)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.longestConsecutive([1,2,0,1]), 3)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.longestConsecutive([]), 0)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.longestConsecutive([1]), 1)
    