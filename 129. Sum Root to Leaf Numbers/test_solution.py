import unittest
from solution import TreeNode, Solution

# help function to create a binary tree from a list
def create_tree(lst, i=0):
    if i >= len(lst) or lst[i] is None:
        return None

    root = TreeNode(lst[i])
    root.left = create_tree(lst, 2*i+1)
    root.right = create_tree(lst, 2*i+2)

    return root

class TestSolution(unittest.TestCase):

    def test_case1(self):
        root = create_tree([1,2,3])
        self.assertEqual(Solution().sumNumbers(root), 25)
    
    def test_case2(self):
        root = create_tree([4,9,0,5,1])
        self.assertEqual(Solution().sumNumbers(root), 1026)
