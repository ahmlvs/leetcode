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


def test_solution():
    solution = Solution()

    # Test 1
    root1 = list_to_binary_tree([3,9,20,None,None,15,7])
    expected1 = 3
    assert solution.maxDepth(root1) == expected1

    # Test 2
    root2 = list_to_binary_tree([1,None,2])
    expected2 = 2
    assert solution.maxDepth(root2) == expected2

    # Test 3
    root3 = list_to_binary_tree([])
    expected3 = 0
    assert solution.maxDepth(root3) == expected3

    print('All tests passed')


if __name__ == '__main__':
    test_solution()
