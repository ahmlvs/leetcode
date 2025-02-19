import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 1
        k = 3
        expected = "c"
        self.assertEqual(sol.getHappyString(n, k), expected)
    
    def test_case_2(self):
        sol = Solution()
        n = 1
        k = 4
        expected = ""
        self.assertEqual(sol.getHappyString(n, k), expected)

    def test_case_3(self):
        sol = Solution()
        n = 3
        k = 9
        expected = "cab"
        self.assertEqual(sol.getHappyString(n, k), expected)
