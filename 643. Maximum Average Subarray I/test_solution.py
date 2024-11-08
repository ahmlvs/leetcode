from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    nums = [1,12,-5,-6,50,3]
    k = 4
    expected = 12.75
    assert solution.findMaxAverage(nums, k) == expected

    # Test 2
    nums = [5]
    k = 1
    expected = 5.0
    assert solution.findMaxAverage(nums, k) == expected

    # Test 3
    nums = [-6,-5,-4,-3,-2,-1]
    k = 2
    expected = -1.5
    assert solution.findMaxAverage(nums, k) == expected

    print('All tests passed')


if __name__ == '__main__':
    test_solution()
