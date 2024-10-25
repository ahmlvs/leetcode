from solution import RecentCounter


def test_solution():
    obj = RecentCounter()

    # Test 1
    assert obj.ping(1) == 1

    # Test 2
    assert obj.ping(100) == 2

    # Test 3
    assert obj.ping(3001) == 3

    # Test 4
    assert obj.ping(3002) == 3

    # Test 5
    assert obj.ping(10000) == 1

    print("All tests passed.")


if __name__ == "__main__":
    test_solution()
