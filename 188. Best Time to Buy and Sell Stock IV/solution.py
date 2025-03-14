# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

# Constraints:

# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000

from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        # if k >= n // 2 it means we sum all profitable differences
        # each day
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
        
        # max profit for each day started from 0
        dp = [[0] * n for _ in range(k+1)]

        # we have 2 variants
        # 1. we do nothing on day. so max profit
        # equal to prev day profit dp[i][j-1]
        # 2. we sell, so we bought before
        # and max profit dp[i-1][p] - prices[p] + prices[j]
        # where  0 <= p < j some day before j
        # and we can calc the best dp[i-1][p] - prices[p] on each iteration
        for i in range(1, k+1):
            # imagine that we bought on 0 day
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], max_diff + prices[j])
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
        
        return dp[k][n-1]
