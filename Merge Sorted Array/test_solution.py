from solution import Solution

def test_solution():
    solution = Solution()
    
    # Test case 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    result1 = solution.merge(nums1, m, nums2, n)
    assert result1 == [1,2,2,3,5,6], f"Expected [1,2,2,3,5,6] but got {result1}"
    
    # Test case 2
    nums3 = [1]
    m = 1
    nums4 = []
    n = 0
    result2 = solution.merge(nums3, m, nums4, n)
    assert result2 == [1], f"Expected [1] but got {result2}"
    
    # Test case 3
    nums5 = [0]
    m = 0
    nums6 = [1]
    n = 1
    result3 = solution.merge(nums5, m, nums6, n)
    assert result3 == [1], f"Expected [1] but got {result3}"

    # Additional test case
    nums7 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums8 = [1, 2, 3]
    n = 3
    result4 = solution.merge(nums7, m, nums8, n)
    assert result4 == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6] but got {result4}"
    
    # Edge case test
    nums9 = [0, 0, 0, 0, 0, 0]
    m = 0
    nums10 = [1, 2, 3, 4, 5, 6]
    n = 6
    result5 = solution.merge(nums9, m, nums10, n)
    assert result5 == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6] but got {result5}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
