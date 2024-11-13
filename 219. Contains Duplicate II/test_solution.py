import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.containsNearbyDuplicate([1,2,3,1], 3), True)
    
    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.containsNearbyDuplicate([1,0,1,1], 1), True)
    
    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2), False)
    