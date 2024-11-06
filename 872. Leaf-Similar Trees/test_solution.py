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
    root1 = list_to_binary_tree([3,5,1,6,2,9,8,None,None,7,4])
    root2 = list_to_binary_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    expected = True
    result = solution.leafSimilar(root1, root2)
    assert result == expected

    # Test 2
    root1 = list_to_binary_tree([1,2,3])
    root2 = list_to_binary_tree([1,3,2])
    expected = False
    result = solution.leafSimilar(root1, root2)
    assert result == expected

    # Test 3
    root1 = list_to_binary_tree([4,2,6,1,3,5,7])
    root2 = list_to_binary_tree([4,2,6,None,3,5,7])
    expected = False
    result = solution.leafSimilar(root1, root2)
    assert result == expected

    print('All tests passed')


if __name__ == '__main__':
    test_solution()
    