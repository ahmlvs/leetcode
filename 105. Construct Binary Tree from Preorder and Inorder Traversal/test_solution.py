import unittest
from solution import Solution, TreeNode

# Helper function to print the tree in level-order for visualization
def tree_to_list(root):
    from collections import deque
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
    # Remove trailing None values for better representation
    while result and result[-1] is None:
        result.pop()
    return result

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
        self.assertEqual(tree_to_list(root), [3, 9, 20, None, None, 15, 7])
    
    def test_case_2(self):
        sol = Solution()
        root = sol.buildTree([-1], [-1])
        self.assertEqual(tree_to_list(root), [-1])
