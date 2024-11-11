import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "anagram"
        t = "nagaram"
        expected = True
        sol = Solution()
        self.assertEqual(sol.isAnagram(s, t), expected)
    
    def test_case_2(self):
        s = "rat"
        t = "car"
        expected = False
        sol = Solution()
        self.assertEqual(sol.isAnagram(s, t), expected)
    
    def test_case_3(self):
        s = "a"
        t = "ab"
        expected = False
        sol = Solution()
        self.assertEqual(sol.isAnagram(s, t), expected)
    