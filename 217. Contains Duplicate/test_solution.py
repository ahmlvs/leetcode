import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1, 2, 3, 1]), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1, 2, 3, 4]), False)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
    
    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1]), False)
    
    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.containsDuplicate([1, 1]), True)
