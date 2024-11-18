import unittest
from solution import TreeNode, Solution
from collections import deque


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

def binary_tree_to_list(root: TreeNode) -> list:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()
    return result


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        root = list_to_binary_tree([3,9,20,None,None,15,7])
        expected_output = [3.00000,14.50000,11.00000]
        output = Solution().averageOfLevels(root)
        self.assertEqual(output, expected_output)
    
    def test_case_2(self):
        root = list_to_binary_tree([3,9,20,15,7])
        expected_output = [3.00000,14.50000,11.00000]
        output = Solution().averageOfLevels(root)
        self.assertEqual(output, expected_output)
    
    def test_case_3(self):
        root = list_to_binary_tree([1])
        expected_output = [1.00000]
        output = Solution().averageOfLevels(root)
        self.assertEqual(output, expected_output)
    