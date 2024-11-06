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
    
    def test_case1(self):
        solution = Solution()
        root = list_to_binary_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = root.left
        q = root.right
        self.assertEqual(solution.lowestCommonAncestor(root, p, q).val, 3)
    
    def test_case2(self):
        solution = Solution()
        root = list_to_binary_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = root.left
        q = root.left.right.right
        self.assertEqual(solution.lowestCommonAncestor(root, p, q).val, 5)
    
    def test_case3(self):
        solution = Solution()
        root = list_to_binary_tree([1,2])
        p = root
        q = root.left
        self.assertEqual(solution.lowestCommonAncestor(root, p, q).val, 1)

    def test_case4(self):
        solution = Solution()
        root = list_to_binary_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = root.left.left
        q = root.left.right.right
        self.assertEqual(solution.lowestCommonAncestor(root, p, q).val, 5)
