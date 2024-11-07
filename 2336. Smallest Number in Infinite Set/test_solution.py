import unittest
from solution import SmallestInfiniteSet

class TestSolution(unittest.TestCase):

    def test_solution(self):
        smallestInfiniteSet = SmallestInfiniteSet()
        smallestInfiniteSet.addBack(2)
        self.assertEqual(smallestInfiniteSet.popSmallest(), 1)
        self.assertEqual(smallestInfiniteSet.popSmallest(), 2)
        self.assertEqual(smallestInfiniteSet.popSmallest(), 3)
        smallestInfiniteSet.addBack(1)
        self.assertEqual(smallestInfiniteSet.popSmallest(), 1)
        self.assertEqual(smallestInfiniteSet.popSmallest(), 4)
        self.assertEqual(smallestInfiniteSet.popSmallest(), 5)
