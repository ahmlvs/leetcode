import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.jump([2,3,1,1,4]), 2)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.jump([2,3,0,1,4]), 2)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.jump([1]), 0)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.jump([1,1,2,1,4]), 3)
    