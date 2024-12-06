# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # n = len(coins)
        # dp = [0] * (n+1)
        # # edge case
        # dp[0] = 0

        # # sort desc
        # sorted_coins = sorted(coins, reverse=True)

        # for i in range(1,n+1):
        #     # from biggest coin to smallest
        #     dp[i] = dp[i-1] + amount // sorted_coins[i-1]
        #     amount = amount % sorted_coins[i-1]
        
        # # finally need to get full amount
        # if amount == 0:
        #     return dp[n]
        # else:
        #     return -1
        
        # # it's not correct
        # # [186,419,83,408] and 6249

        dp = [float('inf')] * (amount+1)
        # 0 coins are needed to make amount 0
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # if dp[amount] == inf
        # no solution
        return dp[amount] if dp[amount] != float('inf') else -1
