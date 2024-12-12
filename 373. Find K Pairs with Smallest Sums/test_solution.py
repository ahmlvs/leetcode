import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.kSmallestPairs([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]])
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.kSmallestPairs([1,1,2], [1,2,3], 2), [[1,1],[1,1]])
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3), [[1,3],[2,3],[1,5]])
