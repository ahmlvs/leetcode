from solution import Solution

def test_solution():
    solution = Solution()

    # Test case 1
    nums = [1,3,5,6]
    target = 5
    assert solution.searchInsert(nums, target) == 2

    # Test case 2
    nums = [1,3,5,6]
    target = 2
    assert solution.searchInsert(nums, target) == 1
    
    # Test case 3
    nums = [1,3,5,6]
    target = 7
    assert solution.searchInsert(nums, target) == 4

    # Test case 4
    nums = [1]
    target = 0
    assert solution.searchInsert(nums, target) == 0

    # Test case 5
    # generate a list of 10^4 elements
    nums = [i for i in range(1, 10001)]
    target = 10001
    assert solution.searchInsert(nums, target) == 10000

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
