import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.trap([4,2,0,3,2,5]), 9)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.trap([1,2,3,4,5]), 0)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.trap([0,0,0,0,0,0,0,0,0,0,0,1]), 0)
