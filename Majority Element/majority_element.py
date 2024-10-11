# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3


# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 
# Follow-up: Could you solve the problem in linear time and in O(1) space?


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Boyer-Moore Voting Algorithm
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        return candidate


def test_majorityElement():
    solution = Solution()
    
    # Test case 1
    nums1 = [3,2,3]
    answer1 = 3
    result1 = solution.majorityElement(nums1)
    assert result1 == answer1, f"Expected {answer1}, but got {result1}"

    # Test case 2
    nums2 = [2,2,1,1,1,2,2]
    answer2 = 2
    result2 = solution.majorityElement(nums2)
    assert result2 == answer2, f"Expected {answer2}, but got {result2}"

    # Test case 3
    nums3 = [1]
    answer3 = 1
    result3 = solution.majorityElement(nums3)
    assert result3 == answer3, f"Expected {answer3}, but got {result3}"

    # Edge case
    num4 = [1,1,2,2]
    answer4 = 1
    result4 = solution.majorityElement(num4)
    assert result4 == answer4, f"Expected {answer4}, but got {result4}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_majorityElement()
