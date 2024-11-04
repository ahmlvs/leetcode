import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "3[a]2[bc]"
        expected = "aaabcbc"
        solution = Solution()
        self.assertEqual(solution.decodeString(s), expected)
    
    def test_case_2(self):
        s = "3[a2[c]]"
        expected = "accaccacc"
        solution = Solution()
        self.assertEqual(solution.decodeString(s), expected)
    
    def test_case_3(self):
        s = "2[abc]3[cd]ef"
        expected = "abcabccdcdcdef"
        solution = Solution()
        self.assertEqual(solution.decodeString(s), expected)
    
    def test_case_4(self):
        s = "3[a]2[bc2[a2[b3[d4[g]]]]]"
        expected = "aaabcabdggggdggggdggggbdggggdggggdggggabdggggdggggdggggbdggggdggggdggggbcabdggggdggggdggggbdggggdggggdggggabdggggdggggdggggbdggggdggggdgggg"
        solution = Solution()
        self.assertEqual(solution.decodeString(s), expected)
