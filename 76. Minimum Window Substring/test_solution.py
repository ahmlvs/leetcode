import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"
        assert Solution().minWindow(s, t) == expected
    
    def test_case_2(self):
        s = "a"
        t = "a"
        expected = "a"
        assert Solution().minWindow(s, t) == expected
    
    def test_case_3(self):
        s = "a"
        t = "aa"
        expected = ""
        assert Solution().minWindow(s, t) == expected
