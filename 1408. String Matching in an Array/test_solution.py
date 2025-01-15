import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        words = ["mass", "as", "hero", "superhero"]
        expected = ["as", "hero"]
        self.assertCountEqual(solution.stringMatching(words), expected)
    
    def test_case_2(self):
        solution = Solution()
        words = ["leetcode", "et", "code"]
        expected = ["et", "code"]
        self.assertCountEqual(solution.stringMatching(words), expected)
    
    def test_case_3(self):
        solution = Solution()
        words = ["blue", "green", "bu"]
        expected = []
        self.assertCountEqual(solution.stringMatching(words), expected)
    
    def test_case_4(self):
        solution = Solution()
        words = ["leetcoder","leetcode","od","hamlet","am"]
        expected = ["leetcode","od","am"]
        self.assertCountEqual(solution.stringMatching(words), expected)
