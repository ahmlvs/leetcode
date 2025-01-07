import unittest
from solution import MedianFinder

class TestSolution(unittest.TestCase):

    def test_example(self):
        # Example 1
        medianFinder = MedianFinder()
        medianFinder.addNum(1)
        medianFinder.addNum(2)
        self.assertEqual(medianFinder.findMedian(), 1.5)
        medianFinder.addNum(3)
        self.assertEqual(medianFinder.findMedian(), 2.0)
