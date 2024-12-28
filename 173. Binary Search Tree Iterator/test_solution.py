import unittest
from solution import BSTIterator, TreeNode

# help function to create a binary tree from a list
def create_tree(lst, i=0):
    if i >= len(lst) or lst[i] is None:
        return None

    root = TreeNode(lst[i])
    root.left = create_tree(lst, 2*i+1)
    root.right = create_tree(lst, 2*i+2)

    return root

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        root = create_tree([7, 3, 15, None, None, 9, 20])
        bSTIterator = BSTIterator(root)
        self.assertEqual(bSTIterator.next(), 3)
        self.assertEqual(bSTIterator.next(), 7)
        self.assertEqual(bSTIterator.hasNext(), True)
        self.assertEqual(bSTIterator.next(), 9)
        self.assertEqual(bSTIterator.hasNext(), True)
        self.assertEqual(bSTIterator.next(), 15)
        self.assertEqual(bSTIterator.hasNext(), True)
        self.assertEqual(bSTIterator.next(), 20)
        self.assertEqual(bSTIterator.hasNext(), False)
