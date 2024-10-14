# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 
# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        
        return k

def test_removeElement():
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    result1 = solution.removeElement(nums1, val1)
    assert result1 == 2, f"Expected 2 but got {result1}"

    # test elements of nums1
    expectedNums1 = [2, 2]
    sorted(nums1[:result1]) # Sort the first k elements of nums
    for i in range(result1):
        assert nums1[i] == expectedNums1[i], f"Expected {expectedNums1} but got {nums1[:result1]}"

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    result2 = solution.removeElement(nums2, val2)
    assert result2 == 5, f"Expected 5 but got {result2}"

    # test elements of nums2
    expectedNums2 = [0, 1 , 3, 0, 4]
    sorted(nums2[:result2]) # Sort the first k elements of nums
    for i in range(result2):
        assert nums2[i] == expectedNums2[i], f"Expected {expectedNums2} but got {nums2[:result2]}"
    
    # Test case 3
    nums3 = [1]
    val3 = 1
    result3 = solution.removeElement(nums3, val3)
    assert result3 == 0, f"Expected 0 but got {result3}"

    expectedNums3 = []
    sorted(nums3[:result3]) # Sort the first k elements of nums
    for i in range(result3):
        assert nums3[i] == expectedNums3[i], f"Expected {expectedNums3} but got {nums3[:result3]}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_removeElement()
