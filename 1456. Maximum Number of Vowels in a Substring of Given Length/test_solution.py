from solution import Solution

def test_case_1():
    solution = Solution()
    s = "abciiidef"
    k = 3
    expected = 3
    result = solution.maxVowels(s, k)
    assert result == expected

def test_case_2():
    solution = Solution()
    s = "aeiou"
    k = 2
    expected = 2
    result = solution.maxVowels(s, k)
    assert result == expected

def test_case_3():
    solution = Solution()
    s = "leetcode"
    k = 3
    expected = 2
    result = solution.maxVowels(s, k)
    assert result == expected
