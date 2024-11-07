# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:

# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

# Constraints:

# 2 <= k <= 9
# 1 <= n <= 60

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, target):
            # need to stop when path has k el
            # and target = 0
            if len(path) == k:
                if target == 0:
                    # append path copy in result
                    # path[:]
                    result.append(path[:])
                # if target not 0 -- not solution
                return
            
            for i in range(start, 10):
                if i > target:
                    break
                # add to combination
                path.append(i)
                # start next combination
                backtrack(i + 1, path, target - i)
                # delete number from comb
                path.pop()

        backtrack(1, [], n)

        return result
