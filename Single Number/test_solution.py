from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    nums = [2, 2, 1]
    expected = 1
    assert solution.singleNumber(nums) == expected

    # Test 2
    nums = [4, 1, 2, 1, 2]
    expected = 4
    assert solution.singleNumber(nums) == expected

    # Test 3
    nums = [1]
    expected = 1
    assert solution.singleNumber(nums) == expected

    # Test 4
    nums = [0, 1, 1]
    expected = 0
    assert solution.singleNumber(nums) == expected

    print('All tests passed')


if __name__ == '__main__':
    test_solution()
