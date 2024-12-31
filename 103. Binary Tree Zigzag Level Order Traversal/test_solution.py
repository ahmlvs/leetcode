import unittest
from solution import TreeNode, Solution

# helper function to create a binary tree from a list
def create_binary_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while i < len(lst):
        current = queue.pop(0)

        if lst[i]:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        
        i += 1

        if i < len(lst) and lst[i]:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        
        i += 1

    return root

# helper function to convert a binary tree to a list
def convert_binary_tree_to_list(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)

        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    
    while result[-1] is None:
        result.pop()
    
    return result


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        root = create_binary_tree([3,9,20,None,None,15,7])
        expected = [[3],[20,9],[15,7]]
        self.assertListEqual(Solution().zigzagLevelOrder(root), expected)
    
    def test_case_2(self):
        root = create_binary_tree([1])
        expected = [[1]]
        self.assertListEqual(Solution().zigzagLevelOrder(root), expected)
    
    def test_case_3(self):
        root = create_binary_tree([])
        expected = []
        self.assertListEqual(Solution().zigzagLevelOrder(root), expected)
