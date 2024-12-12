import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        expected_result = True
        solution = Solution()
        self.assertEqual(solution.isInterleave(s1, s2, s3), expected_result)
    
    def test_case_2(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        expected_result = False
        solution = Solution()
        self.assertEqual(solution.isInterleave(s1, s2, s3), expected_result)
    
    def test_case_3(self):
        s1 = ""
        s2 = ""
        s3 = ""
        expected_result = True
        solution = Solution()
        self.assertEqual(solution.isInterleave(s1, s2, s3), expected_result)
    