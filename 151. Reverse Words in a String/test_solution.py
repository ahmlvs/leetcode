from solution import Solution

def test_case_1():
    solution = Solution()
    s = "the sky is blue"
    expected = "blue is sky the"
    assert solution.reverseWords(s) == expected

def test_case_2():
    solution = Solution()
    s = "  hello world  "
    expected = "world hello"
    assert solution.reverseWords(s) == expected

def test_case_3():
    solution = Solution()
    s = "a good   example"
    expected = "example good a"
    assert solution.reverseWords(s) == expected
