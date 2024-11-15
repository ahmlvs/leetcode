import unittest
from solution import Solution, TreeNode

def tree_to_list(root: TreeNode) -> list:
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    
    while res and res[-1] is None:
        res.pop()
    
    return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        root = sol.sortedArrayToBST([-10,-3,0,5,9])
        expected = [0,-3,9,-10,None,5]
        self.assertEqual(tree_to_list(root), expected)
    
    def test_case_2(self):
        sol = Solution()
        root = sol.sortedArrayToBST([1,3])
        expected = [3,1]
        self.assertEqual(tree_to_list(root), expected)
    
    def test_case_3(self):
        sol = Solution()
        root = sol.sortedArrayToBST([0,1,3,4,5,9])
        expected = [4,1,9,0,3,5]
        self.assertEqual(tree_to_list(root), expected)
