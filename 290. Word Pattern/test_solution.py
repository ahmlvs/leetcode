import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        pattern = "abba"
        s = "dog cat cat dog"
        expected_result = True
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), expected_result)
    
    def test_case_2(self):
        pattern = "abba"
        s = "dog cat cat fish"
        expected_result = False
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), expected_result)
    
    def test_case_3(self):
        pattern = "aaaa"
        s = "dog cat cat dog"
        expected_result = False
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), expected_result)
    
    def test_case_4(self):
        pattern = "abba"
        s = "dog dog dog dog"
        expected_result = False
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), expected_result)
    
    def test_case_5(self):
        pattern = "abb"
        s = "dog cat cat dog"
        expected_result = False
        solution = Solution()
        self.assertEqual(solution.wordPattern(pattern, s), expected_result)
    