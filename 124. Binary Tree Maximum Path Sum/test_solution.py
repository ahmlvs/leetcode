import unittest
from solution import TreeNode, Solution
from collections import deque

# help function to build a binary tree from a list
def build_tree(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    
    while queue and index < len(values):
        current = queue.popleft()
        
        # Add left child
        if index < len(values) and values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1
        
        # Add right child
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1
    
    return root

class TestSolution(unittest.TestCase):

    def test_case1(self):
        nodes = [1,2,3]
        root = build_tree(nodes)
        self.assertEqual(Solution().maxPathSum(root), 6)
    
    def test_case2(self):
        nodes = [-10,9,20,None,None,15,7]
        root = build_tree(nodes)
        self.assertEqual(Solution().maxPathSum(root), 42)
    
    def test_case3(self):
        nodes = [5,4,8,11,None,13,4,7,2,None,None,None,1]
        root = build_tree(nodes)
        self.assertEqual(Solution().maxPathSum(root), 48)
    
    def test_case4(self):
        nodes = [2, -1]
        root = build_tree(nodes)
        self.assertEqual(Solution().maxPathSum(root), 2)
    
    def test_case5(self):
        nodes = [-1000]
        root = build_tree(nodes)
        self.assertEqual(Solution().maxPathSum(root), -1000)
