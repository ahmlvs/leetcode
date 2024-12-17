import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        result = sol.permute([1, 2, 3])
        self.assertEqual(result, [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    
    def test_case_2(self):
        sol = Solution()
        result = sol.permute([0, 1])
        self.assertEqual(result, [[0, 1], [1, 0]])
    
    def test_case_3(self):
        sol = Solution()
        result = sol.permute([1])
        self.assertEqual(result, [[1]])
