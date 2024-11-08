from solution import Solution


def test_solution():

    # Test case 1
    n1 = 10
    pick1 = 6
    solution1 = Solution(pick1)
    assert solution1.guessNumber(n1) == pick1

    # Test case 2
    n2 = 1
    pick2 = 1
    solution2 = Solution(pick2)
    assert solution2.guessNumber(n2) == pick2

    # Test case 3
    n3 = 2
    pick3 = 1
    solution3 = Solution(pick3)
    assert solution3.guessNumber(n3) == pick3

    # Additional test cases
    n4 = 1000
    pick4 = 1000
    solution4 = Solution(pick4)
    assert solution4.guessNumber(n4) == pick4

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
