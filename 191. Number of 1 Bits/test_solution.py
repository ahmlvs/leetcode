import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.hammingWeight(11), 3)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.hammingWeight(128), 1)

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.hammingWeight(2147483645), 30)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.hammingWeight(0), 0)
    