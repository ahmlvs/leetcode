from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    expected = [[1, 3], [4, 6]]
    result = solution.findDifference(nums1, nums2)
    assert result == expected

    # Test 2
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    expected = [[3], []]
    result = solution.findDifference(nums1, nums2)
    assert result == expected

    # Test 3
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    expected = [[], []]
    result = solution.findDifference(nums1, nums2)
    assert result == expected

    print("All tests passed")


if __name__ == "__main__":
    test_solution()
