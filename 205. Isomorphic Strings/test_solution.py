import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "egg"
        t = "add"
        expected_result = True
        solution = Solution()
        result = solution.isIsomorphic(s, t)
        self.assertEqual(result, expected_result)
    
    def test_case_2(self):
        s = "foo"
        t = "bar"
        expected_result = False
        solution = Solution()
        result = solution.isIsomorphic(s, t)
        self.assertEqual(result, expected_result)
    
    def test_case_3(self):
        s = "paper"
        t = "title"
        expected_result = True
        solution = Solution()
        result = solution.isIsomorphic(s, t)
        self.assertEqual(result, expected_result)
    
    def test_case_4(self):
        s = "egg"
        t = "foo"
        expected_result = True
        solution = Solution()
        result = solution.isIsomorphic(s, t)
        self.assertEqual(result, expected_result)
    
    def test_case_5(self):
        s = "bbbaaaba"
        t = "aaabbbba"
        expected_result = False
        solution = Solution()
        result = solution.isIsomorphic(s, t)
        self.assertEqual(result, expected_result)
