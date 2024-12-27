import unittest
from solution import Solution, TreeNode
from collections import deque

# Correct helper functions

def list_to_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root):
    lst = []
    current = root
    while current:
        lst.append(current.val)
        current = current.right
    return lst

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        root = list_to_tree([1, 2, 5, 3, 4, None, 6])
        Solution().flatten(root)
        self.assertEqual(tree_to_list(root), [1, 2, 3, 4, 5, 6])

    def test_case_2(self):
        root = list_to_tree([])
        Solution().flatten(root)
        self.assertEqual(tree_to_list(root), [])

    def test_case_3(self):
        root = list_to_tree([0])
        Solution().flatten(root)
        self.assertEqual(tree_to_list(root), [0])
