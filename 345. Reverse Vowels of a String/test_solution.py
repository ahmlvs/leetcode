from solution import Solution

def test_solution():
    solution = Solution()

    # Test 1
    s1 = "IceCreAm"
    expected1 = "AceCreIm"
    assert solution.reverseVowels(s1) == expected1

    # Test 2
    s2 = "leetcode"
    expected2 = "leotcede"
    assert solution.reverseVowels(s2) == expected2

    # Test 3
    s3 = "aa"
    expected3 = "aa"
    assert solution.reverseVowels(s3) == expected3

    # Test 4
    s4 = "aA"
    expected4 = "Aa"
    assert solution.reverseVowels(s4) == expected4

    print("All tests passed.")


if __name__ == '__main__':
    test_solution()
