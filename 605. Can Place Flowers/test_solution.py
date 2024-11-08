from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    assert solution.canPlaceFlowers(flowerbed1, n1) == True

    # Test 2
    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    assert solution.canPlaceFlowers(flowerbed2, n2) == False

    # Test 3
    flowerbed3 = [0, 0, 1, 0, 0]
    n3 = 2
    assert solution.canPlaceFlowers(flowerbed3, n3) == True

    # Test 4
    flowerbed4 = [0, 0, 0, 0, 0]
    n4 = 3
    assert solution.canPlaceFlowers(flowerbed4, n4) == True

    # Test 5
    flowerbed5 = [0, 0]
    n5 = 1
    assert solution.canPlaceFlowers(flowerbed5, n5) == True

    print("All tests passed")


if __name__ == "__main__":
    test_solution()
