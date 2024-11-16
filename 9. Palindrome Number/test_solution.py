import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(121), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(-121), False)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(10), False)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(0), True)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(1001), True)
    
    def test_case_6(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(10101), True)
    
    def test_case_7(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(1010001), False)
        