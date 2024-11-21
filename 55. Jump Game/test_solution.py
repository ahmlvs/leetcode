import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.canJump([2,3,1,1,4]), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.canJump([3,2,1,0,4]), False)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.canJump([0]), True)
    