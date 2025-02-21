import unittest
from solution import FindElements, TreeNode

class TestFindElements(unittest.TestCase):

    def test_case_1(self):
        findElements = FindElements(TreeNode(-1, None, TreeNode(-1)))
        self.assertEqual(findElements.find(1), False)
        self.assertEqual(findElements.find(2), True)
    
    def test_case_2(self):
        findElements = FindElements(TreeNode(-1, TreeNode(-1), TreeNode(-1)))
        self.assertEqual(findElements.find(1), True)
        self.assertEqual(findElements.find(3), False)
        self.assertEqual(findElements.find(5), False)
    
    def test_case_3(self):
        findElements = FindElements(TreeNode(-1, None, TreeNode(-1, TreeNode(-1), None)))
        self.assertEqual(findElements.find(2), True)
        self.assertEqual(findElements.find(3), False)
        self.assertEqual(findElements.find(4), False)
        self.assertEqual(findElements.find(5), True)
