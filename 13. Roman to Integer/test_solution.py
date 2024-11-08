from solution import Solution

def test_solution():
    solution = Solution()
    
    # Test case 1
    s1 = "III"
    answer1 = 3
    result1 = solution.romanToInt(s1)
    assert result1 == answer1, f"Expected {answer1}, but got {result1}"

    # Test case 2
    s2 = "LVIII"
    answer2 = 58
    result2 = solution.romanToInt(s2)
    assert result2 == answer2, f"Expected {answer2}, but got {result2}"

    # Test case 3
    s3 = "MCMXCIV"
    answer3 = 1994
    result3 = solution.romanToInt(s3)
    assert result3 == answer3, f"Expected {answer3}, but got {result3}"

    # Test case 4
    s4 = "X"
    answer4 = 10
    result4 = solution.romanToInt(s4)
    assert result4 == answer4, f"Expected {answer4}, but got {result4}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
