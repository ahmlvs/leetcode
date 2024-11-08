import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        s = Solution()
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        searchWord = "mouse"
        expected = [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
                    ["mouse", "mousepad"], ["mouse", "mousepad"]]
        self.assertEqual(s.suggestedProducts(products, searchWord), expected)

    def test_2(self):
        s = Solution()
        products = ["havana"]
        searchWord = "havana"
        expected = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
        self.assertEqual(s.suggestedProducts(products, searchWord), expected)
    
    def test_3(self):
        s = Solution()
        products = ["bags","baggage","banner","box","cloths"]
        searchWord = "bags"
        expected = [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
        self.assertEqual(s.suggestedProducts(products, searchWord), expected)
