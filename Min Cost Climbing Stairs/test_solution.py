from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    cost = [10, 15, 20]
    expected = 15
    result = solution.minCostClimbingStairs(cost)
    assert result == expected

    # Test 2
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    expected = 6
    result = solution.minCostClimbingStairs(cost)
    assert result == expected

    # Test 3
    cost = [1, 0, 0, 0]
    expected = 0
    result = solution.minCostClimbingStairs(cost)
    assert result == expected

    print("All tests passed.")


if __name__ == "__main__":
    test_solution()
