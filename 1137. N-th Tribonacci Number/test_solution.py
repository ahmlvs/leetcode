from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    n = 4
    expected = 4
    result = solution.tribonacci(n)
    assert result == expected

    # Test 2
    n = 25
    expected = 1389537
    result = solution.tribonacci(n)
    assert result == expected

    # Test 3
    n = 0
    expected = 0
    result = solution.tribonacci(n)
    assert result == expected

    print("All tests passed")


if __name__ == "__main__":
    test_solution()
