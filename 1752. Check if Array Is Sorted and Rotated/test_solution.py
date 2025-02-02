import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.check([3,4,5,1,2]), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.check([2,1,3,4]), False)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.check([1,2,3]), True)
