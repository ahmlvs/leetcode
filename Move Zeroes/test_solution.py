from solution import Solution

def test_solution():
    solution = Solution()

    # Test 1
    nums1 = [0,1,0,3,12]
    solution.moveZeroes(nums1)
    assert nums1 == [1,3,12,0,0]

    # Test 2
    nums2 = [0]
    solution.moveZeroes(nums2)
    assert nums2 == [0]

    # Test 3
    nums3 = [0,0,1]
    solution.moveZeroes(nums3)
    assert nums3 == [1,0,0]

    # Test 4
    nums4 = [1,0,0]
    solution.moveZeroes(nums4)
    assert nums4 == [1,0,0]

    print('All tests passed')

if __name__ == '__main__':
    test_solution()
