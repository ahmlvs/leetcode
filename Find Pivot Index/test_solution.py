from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    nums1 = [1, 7, 3, 6, 5, 6]
    expected1 = 3
    assert solution.pivotIndex(nums1) == expected1

    # Test 2
    nums2 = [1, 2, 3]
    expected2 = -1
    assert solution.pivotIndex(nums2) == expected2

    # Test 3
    nums3 = [2, 1, -1]
    expected3 = 0
    assert solution.pivotIndex(nums3) == expected3

    # Test 4
    nums4 = [-1,-1,-1,-1,0,1]
    expected4 = 1
    assert solution.pivotIndex(nums4) == expected4

    print("All tests passed.")


if __name__ == "__main__":
    test_solution()
