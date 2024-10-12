# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 
# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        actual_index = 0
        actual_value = None

        for i, num in enumerate(nums):
            if num != actual_value:
                nums[actual_index] = num
                actual_value = num
                actual_index += 1
        
        for i in range(actual_index, len(nums)):
            nums[i] = "_"

        # print(nums, actual_index)
        return actual_index
            


def test_removeDuplicates():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 2]
    result1 = solution.removeDuplicates(nums1)
    assert result1 == 2, f"Expected 2 but got {result1}"

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result2 = solution.removeDuplicates(nums2)
    assert result2 == 5, f"Expected 5 but got {result2}"

    # Test case 3
    nums3 = [1, 2, 3]
    result3 = solution.removeDuplicates(nums3)
    assert result3 == 3, f"Expected 3 but got {result3}"

    # Test case 4
    nums4 = [1, 1, 1, 1, 1]
    result4 = solution.removeDuplicates(nums4)
    assert result4 == 1, f"Expected 1 but got {result4}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_removeDuplicates()
