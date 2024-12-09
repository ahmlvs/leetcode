import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.minimumTotal([[-10]]), -10)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.minimumTotal([[2],[3,4],[6,2,1],[4,2,2,1]]), 8)
