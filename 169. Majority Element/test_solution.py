from solution import Solution

def test_solution():
    solution = Solution()
    
    # Test case 1
    nums1 = [3,2,3]
    answer1 = 3
    result1 = solution.majorityElement(nums1)
    assert result1 == answer1, f"Expected {answer1}, but got {result1}"

    # Test case 2
    nums2 = [2,2,1,1,1,2,2]
    answer2 = 2
    result2 = solution.majorityElement(nums2)
    assert result2 == answer2, f"Expected {answer2}, but got {result2}"

    # Test case 3
    nums3 = [1]
    answer3 = 1
    result3 = solution.majorityElement(nums3)
    assert result3 == answer3, f"Expected {answer3}, but got {result3}"

    # Edge case
    num4 = [1,1,2,2]
    answer4 = 1
    result4 = solution.majorityElement(num4)
    assert result4 == answer4, f"Expected {answer4}, but got {result4}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
