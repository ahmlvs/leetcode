import unittest
from solution import ProductOfNumbers


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        productOfNumbers = ProductOfNumbers()
        productOfNumbers.add(3)
        productOfNumbers.add(0)
        productOfNumbers.add(2)
        productOfNumbers.add(5)
        productOfNumbers.add(4)
        self.assertEqual(20, productOfNumbers.getProduct(2))
        self.assertEqual(40, productOfNumbers.getProduct(3))
        self.assertEqual(0, productOfNumbers.getProduct(4))
        productOfNumbers.add(8)
        self.assertEqual(32, productOfNumbers.getProduct(2))
