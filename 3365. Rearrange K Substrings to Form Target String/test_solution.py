import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "abcd"
        t = "cdab"
        k = 2
        expected = True
        solution = Solution()
        self.assertEqual(solution.isPossibleToRearrange(s, t, k), expected)
    
    def test_case_2(self):
        s = "aabbcc"
        t = "bbaacc"
        k = 3
        expected = True
        solution = Solution()
        self.assertEqual(solution.isPossibleToRearrange(s, t, k), expected)
    
    def test_case_3(self):
        s = "aabbcc"
        t = "bbaacc"
        k = 2
        expected = False
        solution = Solution()
        self.assertEqual(solution.isPossibleToRearrange(s, t, k), expected)
    
    def test_case_4(self):
        s = "nc"
        t = "cn"
        k = 1
        expected = False
        solution = Solution()
        self.assertEqual(solution.isPossibleToRearrange(s, t, k), expected)
    
    def test_case_5(self):
        s = "jvdk"
        t = "vjdk"
        k = 2
        expected = False
        solution = Solution()
        self.assertEqual(solution.isPossibleToRearrange(s, t, k), expected)
    