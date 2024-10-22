from solution import Solution

def test_solution():
    solution = Solution()

    # Test case 1
    word1 = "abc"
    word2 = "pqr"
    result1 = solution.mergeAlternately(word1, word2)
    assert result1 == "apbqcr", f"Expected 'apbqcr' but got {result1}"

    # Test case 2
    word3 = "ab"
    word4 = "pqrs"
    result2 = solution.mergeAlternately(word3, word4)
    assert result2 == "apbqrs", f"Expected 'apbqrs' but got {result2}"

    # Test case 3
    word5 = "abcd"
    word6 = "pq"
    result3 = solution.mergeAlternately(word5, word6)
    assert result3 == "apbqcd", f"Expected 'apbqcd' but got {result3}"

    # Additional test case
    word7 = "a"
    word8 = "b"
    result4 = solution.mergeAlternately(word7, word8)
    assert result4 == "ab", f"Expected 'ab' but got {result4}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
