import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        path = "/home/"
        expected = "/home"
        s = Solution()
        self.assertEqual(s.simplifyPath(path), expected)
    
    def test_case_2(self):
        path = "/home//foo/"
        expected = "/home/foo"
        s = Solution()
        self.assertEqual(s.simplifyPath(path), expected)
    
    def test_case_3(self):
        path = "/home/user/Documents/../Pictures"
        expected = "/home/user/Pictures"
        s = Solution()
        self.assertEqual(s.simplifyPath(path), expected)
    
    def test_case_4(self):
        path = "/../"
        expected = "/"
        s = Solution()
        self.assertEqual(s.simplifyPath(path), expected)
    
    def test_case_5(self):
        path = "/.../a/../b/c/../d/./"
        expected = "/.../b/d"
        s = Solution()
        self.assertEqual(s.simplifyPath(path), expected)
    
    def test_case_6(self):
        path = "/a/./b/../../c/"
        expected = "/c"
        s = Solution()
        self.assertEqual(s.simplifyPath(path), expected)
