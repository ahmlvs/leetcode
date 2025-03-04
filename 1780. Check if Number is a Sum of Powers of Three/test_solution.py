import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.checkPowersOfThree(12), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.checkPowersOfThree(91), True)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.checkPowersOfThree(21), False)
