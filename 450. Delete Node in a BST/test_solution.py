import unittest
from solution import Solution
from solution import TreeNode
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
    def test_1(self):
        solution = Solution()
        root = list_to_binary_tree([5, 3, 6, 2, 4, None, 7])
        key = 3
        expected = [5, 4, 6, 2, None, None, 7]
        output = binary_tree_to_list(solution.deleteNode(root, key))
        self.assertEqual(output, expected)
    
    def test_2(self):
        solution = Solution()
        root = list_to_binary_tree([5, 3, 6, 2, 4, None, 7])
        key = 0
        expected = [5, 3, 6, 2, 4, None, 7]
        output = binary_tree_to_list(solution.deleteNode(root, key))
        self.assertEqual(output, expected)
    
    def test_3(self):
        solution = Solution()
        root = list_to_binary_tree([])
        key = 0
        expected = []
        output = binary_tree_to_list(solution.deleteNode(root, key))
        self.assertEqual(output, expected)
    
    def test_4(self):
        solution = Solution()
        root = list_to_binary_tree([0])
        key = 0
        expected = []
        output = binary_tree_to_list(solution.deleteNode(root, key))
        self.assertEqual(output, expected)
    
    def test_5(self):
        solution = Solution()
        root = list_to_binary_tree([5,3,6,2,4,None,7])
        key = 7
        expected = [5,3,6,2,4]
        output = binary_tree_to_list(solution.deleteNode(root, key))
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
