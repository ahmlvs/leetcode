import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.minFlips(2, 6, 5), 3)
    
    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.minFlips(4, 2, 7), 1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.minFlips(1, 2, 3), 0)
