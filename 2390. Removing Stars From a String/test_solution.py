from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    s = "leet**cod*e"
    expected = "lecoe"
    result = solution.removeStars(s)
    assert result == expected

    # Test 2
    s = "erase*****"
    expected = ""
    result = solution.removeStars(s)
    assert result == expected

    # Test 3
    s = "a**b"
    expected = "b"
    result = solution.removeStars(s)
    assert result == expected

    print("All tests passed!")


if __name__ == '__main__':
    test_solution()
