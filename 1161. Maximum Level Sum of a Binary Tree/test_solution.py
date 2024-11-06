import unittest
from solution import Solution
from solution import TreeNode

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
    def test_1(self):
        solution = Solution()
        root = list_to_binary_tree([1,7,0,7,-8,None,None])
        self.assertEqual(solution.maxLevelSum(root), 2)
    
    def test_2(self):
        solution = Solution()
        root = list_to_binary_tree([989,None,10250,98693,-89388,None,None,None,-32127])
        self.assertEqual(solution.maxLevelSum(root), 2)

if __name__ == '__main__':
    unittest.main()
