from solution import Solution

def test_solution():
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    result1 = solution.removeElement(nums1, val1)
    assert result1 == 2, f"Expected 2 but got {result1}"

    # test elements of nums1
    expectedNums1 = [2, 2]
    sorted(nums1[:result1]) # Sort the first k elements of nums
    for i in range(result1):
        assert nums1[i] == expectedNums1[i], f"Expected {expectedNums1} but got {nums1[:result1]}"

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    result2 = solution.removeElement(nums2, val2)
    assert result2 == 5, f"Expected 5 but got {result2}"

    # test elements of nums2
    expectedNums2 = [0, 1 , 3, 0, 4]
    sorted(nums2[:result2]) # Sort the first k elements of nums
    for i in range(result2):
        assert nums2[i] == expectedNums2[i], f"Expected {expectedNums2} but got {nums2[:result2]}"
    
    # Test case 3
    nums3 = [1]
    val3 = 1
    result3 = solution.removeElement(nums3, val3)
    assert result3 == 0, f"Expected 0 but got {result3}"

    expectedNums3 = []
    sorted(nums3[:result3]) # Sort the first k elements of nums
    for i in range(result3):
        assert nums3[i] == expectedNums3[i], f"Expected {expectedNums3} but got {nums3[:result3]}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
