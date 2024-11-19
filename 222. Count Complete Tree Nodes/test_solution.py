import unittest
from solution import TreeNode, Solution

# Helper function to create a binary tree from a list (level-order)
def list_to_binary_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = Solution()
        root = list_to_binary_tree([1, 2, 3, 4, 5, 6])
        self.assertEqual(s.countNodes(root), 6)
    
    def test_case_2(self):
        s = Solution()
        root = list_to_binary_tree([])
        self.assertEqual(s.countNodes(root), 0)
    
    def test_case_3(self):
        s = Solution()
        root = list_to_binary_tree([1])
        self.assertEqual(s.countNodes(root), 1)
    
    def test_case_4(self):
        s = Solution()
        root = list_to_binary_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(s.countNodes(root), 7)
    