from solution import Solution

def test_solution():
    solution = Solution()

    # Test case 1
    str1 = "ABCABC"
    str2 = "ABC"
    assert solution.gcdOfStrings(str1, str2) == "ABC"

    # Test case 2
    str1 = "ABABAB"
    str2 = "ABAB"
    assert solution.gcdOfStrings(str1, str2) == "AB"

    # Test case 3
    str1 = "LEET"
    str2 = "CODE"
    assert solution.gcdOfStrings(str1, str2) == ""

    # Test case 4
    str1 = "A"
    str2 = "A"
    assert solution.gcdOfStrings(str1, str2) == "A"

    print("All test cases passed!")
