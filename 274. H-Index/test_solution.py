import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([3,0,6,1,5]), 3)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([1,3,1]), 1)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([0, 0, 0, 0]), 0)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([0, 0, 0, 1]), 1)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.hIndex([6,6,6,6,6,6]), 6)
    