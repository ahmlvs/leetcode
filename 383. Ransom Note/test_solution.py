import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_canConstruct(self):
        solution = Solution()
        self.assertEqual(solution.canConstruct("a", "b"), False)
    
    def test_canConstruct_1(self):
        solution = Solution()
        self.assertEqual(solution.canConstruct("aa", "ab"), False)
    
    def test_canConstruct_2(self):
        solution = Solution()
        self.assertEqual(solution.canConstruct("aa", "aab"), True)
        