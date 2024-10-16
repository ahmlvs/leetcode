# test_remove_duplicates_from_sorted_array.py

from remove_duplicates_from_sorted_array import Solution

def test_solution():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 2]
    result1 = solution.removeDuplicates(nums1)
    assert result1 == 2, f"Expected 2 but got {result1}"

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result2 = solution.removeDuplicates(nums2)
    assert result2 == 5, f"Expected 5 but got {result2}"

    # Test case 3
    nums3 = [1, 2, 3]
    result3 = solution.removeDuplicates(nums3)
    assert result3 == 3, f"Expected 3 but got {result3}"

    # Test case 4
    nums4 = [1, 1, 1, 1, 1]
    result4 = solution.removeDuplicates(nums4)
    assert result4 == 1, f"Expected 1 but got {result4}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
