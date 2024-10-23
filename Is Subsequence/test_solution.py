from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    s1 = "abc"
    t1 = "ahbgdc"
    assert solution.isSubsequence(s1, t1) == True

    # Test 2
    s2 = "axc"
    t2 = "ahbgdc"
    assert solution.isSubsequence(s2, t2) == False

    # Test 3
    s3 = ""
    t3 = "ahbgdc"
    assert solution.isSubsequence(s3, t3) == True

    # Test 4
    s4 = "abc"
    t4 = ""
    assert solution.isSubsequence(s4, t4) == False

    # Test 5
    s5 = ""
    t5 = ""
    assert solution.isSubsequence(s5, t5) == True

    print("All tests passed")


if __name__ == "__main__":
    test_solution()
