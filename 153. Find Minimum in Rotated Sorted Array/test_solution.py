import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.findMin([3,4,5,1,2]), 1)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.findMin([4,5,6,7,0,1,2]), 0)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.findMin([11,13,15,17]), 11)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.findMin([1]), 1)
    