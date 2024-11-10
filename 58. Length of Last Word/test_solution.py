import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_lengthOfLastWord(self):
        s = "Hello World"
        expected = 5
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), expected)
    
    def test_lengthOfLastWord_2(self):
        s = "   fly me   to   the moon  "
        expected = 4
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), expected)
    
    def test_lengthOfLastWord_3(self):
        s = "luffy is still joyboy"
        expected = 6
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), expected)
