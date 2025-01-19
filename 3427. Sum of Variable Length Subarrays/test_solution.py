import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.subarraySum([2,3,1]), 11)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.subarraySum([3,1,1,2]), 13)
