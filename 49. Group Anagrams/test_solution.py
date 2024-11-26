import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        self.assertEqual(result, [["eat","tea","ate"],["tan","nat"],["bat"]])
    
    def test_case_2(self):
        solution = Solution()
        result = solution.groupAnagrams([""])
        self.assertEqual(result, [[""]])
    
    def test_case_3(self):
        solution = Solution()
        result = solution.groupAnagrams(["a"])
        self.assertEqual(result, [["a"]])
    