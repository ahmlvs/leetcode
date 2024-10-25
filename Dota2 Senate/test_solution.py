from solution import Solution


def test_solution():
    solution = Solution()

    # Test 1
    senate = "RD"
    assert solution.predictPartyVictory(senate) == "Radiant"

    # Test 2
    senate = "RDD"
    assert solution.predictPartyVictory(senate) == "Dire"

    # Test 3
    senate = "DDRRR"
    assert solution.predictPartyVictory(senate) == "Dire"

    # Test 4
    senate = "DDDD"
    assert solution.predictPartyVictory(senate) == "Dire"

    print('All tests passed')


if __name__ == '__main__':
    test_solution()
