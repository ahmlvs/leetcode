from solution import Solution

def test_case_1():
    solution = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    assert solution.uniqueOccurrences(arr) == True

def test_case_2():
    solution = Solution()
    arr = [1, 2]
    assert solution.uniqueOccurrences(arr) == False

def test_case_3():
    solution = Solution()
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    assert solution.uniqueOccurrences(arr) == True
