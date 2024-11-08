from solution import Solution

def test_solution():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    assert result1 == [0, 1], f"Expected [0, 1] but got {result1}"
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    assert result2 == [1, 2], f"Expected [1, 2] but got {result2}"
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    assert result3 == [0, 1], f"Expected [0, 1] but got {result3}"

    # Additional test case
    nums4 = [1, 5, 3, 8]
    target4 = 8
    result4 = solution.twoSum(nums4, target4)
    assert result4 == [1, 2], f"Expected [1, 3] but got {result4}"
    
    # Edge case test
    nums5 = [0, 4, 3, 0]
    target5 = 0
    result5 = solution.twoSum(nums5, target5)
    assert result5 == [0, 3], f"Expected [0, 3] but got {result5}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
