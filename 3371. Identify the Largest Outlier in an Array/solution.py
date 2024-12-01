# You are given an integer array nums. This array contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.

# An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

# Note that special numbers, the sum element, and the outlier must have distinct indices, but may share the same value.

# Return the largest potential outlier in nums.

 

# Example 1:

# Input: nums = [2,3,5,10]

# Output: 10

# Explanation:

# The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.

# Example 2:

# Input: nums = [-2,-1,-3,-6,4]

# Output: 4

# Explanation:

# The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.

# Example 3:

# Input: nums = [1,1,1,1,1,5,5]

# Output: 5

# Explanation:

# The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.

 

# Constraints:

# 3 <= nums.length <= 105
# -1000 <= nums[i] <= 1000
# The input is generated such that at least one potential outlier exists in nums.

from collections import Counter
from typing import List

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        sum_total = sum(nums)
        nums_counts = Counter(nums)
        outliers = set()

        # sum_total = sum(specials) + sum_specials + outlier
        # sum(specials) = sum_specials
        # outlier = sum_total - 2*sum_specials

        for num in nums:
            sum_specials = num
            outlier = sum_total - 2 * sum_specials

            # must have distinct indices
            nums_counts[sum_specials] -= 1
            if nums_counts[outlier] > 0:
                outliers.add(outlier)
            nums_counts[sum_specials] += 1

        return max(outliers)
