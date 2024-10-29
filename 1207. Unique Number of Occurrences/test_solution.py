from solution import Solution

def test_solution():
    solution = Solution()

    # Test case 1
    arr = [1,2,2,1,1,3]
    assert solution.uniqueOccurrences(arr) == True

    # Test case 2
    arr = [1,2]
    assert solution.uniqueOccurrences(arr) == False

    # Test case 3
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    assert solution.uniqueOccurrences(arr) == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
