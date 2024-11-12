import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_isValid(self):
        s = "()"
        output = True
        self.assertEqual(Solution().isValid(s), output)
    
    def test_isValid_2(self):
        s = "()[]{}"
        output = True
        self.assertEqual(Solution().isValid(s), output)
    
    def test_isValid_3(self):
        s = "(]"
        output = False
        self.assertEqual(Solution().isValid(s), output)
    
    def test_isValid_4(self):
        s = "([])"
        output = True
        self.assertEqual(Solution().isValid(s), output)
    
    def test_isValid_5(self):
        s = "([)]"
        output = False
        self.assertEqual(Solution().isValid(s), output)
    