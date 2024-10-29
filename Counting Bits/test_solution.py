from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    n = 2
    expected = [0, 1, 1]
    assert solution.countBits(n) == expected

    # Test 2
    n = 5
    expected = [0, 1, 1, 2, 1, 2]
    assert solution.countBits(n) == expected

    # Test 3
    n = 0
    expected = [0]
    assert solution.countBits(n) == expected

    # Test 4
    n = 1
    expected = [0, 1]
    assert solution.countBits(n) == expected

    print('All tests passed')


if __name__ == '__main__':
    test_solution()
