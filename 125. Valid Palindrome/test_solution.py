import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "A man, a plan, a canal: Panama"
        expected_result = True
        solution = Solution()
        result = solution.isPalindrome(s)
        self.assertEqual(result, expected_result)
    
    def test_case_2(self):
        s = "race a car"
        expected_result = False
        solution = Solution()
        result = solution.isPalindrome(s)
        self.assertEqual(result, expected_result)
    
    def test_case_3(self):
        s = " "
        expected_result = True
        solution = Solution()
        result = solution.isPalindrome(s)
        self.assertEqual(result, expected_result)
        