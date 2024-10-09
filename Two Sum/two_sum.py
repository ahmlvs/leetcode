# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_to_index = {}

        for i, num in enumerate(nums):
            part = target - num
            if part in num_to_index:
                return [num_to_index[part], i]
            num_to_index[num] = i


def test_twoSum():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    assert result1 == [0, 1], f"Expected [0, 1] but got {result1}"
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    assert result2 == [1, 2], f"Expected [1, 2] but got {result2}"
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    assert result3 == [0, 1], f"Expected [0, 1] but got {result3}"

    # Additional test case
    nums4 = [1, 5, 3, 8]
    target4 = 8
    result4 = solution.twoSum(nums4, target4)
    assert result4 == [1, 2], f"Expected [1, 3] but got {result4}"
    
    # Edge case test
    nums5 = [0, 4, 3, 0]
    target5 = 0
    result5 = solution.twoSum(nums5, target5)
    assert result5 == [0, 3], f"Expected [0, 3] but got {result5}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_twoSum()
