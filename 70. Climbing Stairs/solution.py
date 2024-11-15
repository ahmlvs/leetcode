# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45


class Solution:
    def climbStairs(self, n: int) -> int:
        # or from n-1 with 1 step
        # or from n-2 with 2 step
        # so dp(n)=dp(n-1)+dp(n-2)

        # dp with 1's
        dp = [1] * (n+1)

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        # answer in n
        return dp[n]
