import unittest
from solution import Solution

def test_case_1():
    solution = Solution()
    assert solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]

def test_case_2():
    solution = Solution()
    assert solution.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

def test_case_3():
    solution = Solution()
    assert solution.productExceptSelf([1,0]) == [0,1]

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_case_2(self):
        self.assertEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_case_3(self):
        self.assertEqual(self.solution.productExceptSelf([1, 0]), [0, 1])
