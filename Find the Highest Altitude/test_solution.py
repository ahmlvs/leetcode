from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    gain1 = [-5, 1, 5, 0, -7]
    expected1 = 1
    assert solution.largestAltitude(gain1) == expected1

    # Test 2
    gain2 = [-4, -3, -2, -1, 4, 3, 2]
    expected2 = 0
    assert solution.largestAltitude(gain2) == expected2

    # Test 3
    gain3 = [1, 2, 3, 4, 5]
    expected3 = 15
    assert solution.largestAltitude(gain3) == expected3

    print("All tests passed")


if __name__ == "__main__":
    test_solution()
