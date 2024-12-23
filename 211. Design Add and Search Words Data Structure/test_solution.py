import unittest
from solution import WordDictionary


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        self.assertEqual(False, wordDictionary.search("pad"))
        self.assertEqual(True, wordDictionary.search("bad"))
        self.assertEqual(True, wordDictionary.search(".ad"))
        self.assertEqual(True, wordDictionary.search("b.."))

    def test_case_2(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("a")
        wordDictionary.addWord("a")
        self.assertEqual(True, wordDictionary.search("."))
        self.assertEqual(True, wordDictionary.search("a"))
        self.assertEqual(False, wordDictionary.search("aa"))
        self.assertEqual(True, wordDictionary.search("a"))
        self.assertEqual(True, wordDictionary.search("."))

    def test_case_3(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("at")
        wordDictionary.addWord("and")
        wordDictionary.addWord("an")
        wordDictionary.addWord("add")
        self.assertEqual(False, wordDictionary.search("a"))
        self.assertEqual(False, wordDictionary.search(".at"))
        wordDictionary.addWord("bat")
        self.assertEqual(True, wordDictionary.search(".at"))
        self.assertEqual(True, wordDictionary.search("an."))
        self.assertEqual(False, wordDictionary.search("a.d."))
        self.assertEqual(False, wordDictionary.search("b."))
        self.assertEqual(True, wordDictionary.search("a.d"))
        self.assertEqual(False, wordDictionary.search("."))
        self.assertEqual(True, wordDictionary.search(".."))
