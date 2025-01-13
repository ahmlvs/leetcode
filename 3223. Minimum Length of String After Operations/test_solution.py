import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "abaacbcbb"
        expected = 5
        self.assertEqual(sol.minimumLength(s), expected)
    
    def test_case_2(self):
        sol = Solution()
        s = "aa"
        expected = 2
        self.assertEqual(sol.minimumLength(s), expected)
    
    def test_case_3(self):
        sol = Solution()
        s = "a"
        expected = 1
        self.assertEqual(sol.minimumLength(s), expected)
    
    def test_case_4(self):
        sol = Solution()
        s = "ab"
        expected = 2
        self.assertEqual(sol.minimumLength(s), expected)
    
    def test_case_5(self):
        sol = Solution()
        s = "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"
        expected = 38
        self.assertEqual(sol.minimumLength(s), expected)
