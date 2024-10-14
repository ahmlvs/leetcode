# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        max_profit = 0

        for i in range(1, len(prices)):
            profit += prices[i] - prices[i-1]
            if profit < 0:
                profit = 0
            
            if max_profit < profit:
                max_profit = profit
        
        return max_profit


def test_maxProfit():
    solution = Solution()

    # Test case 1
    prices1 = [7,1,5,3,6,4]
    answer1 = 5
    result1 = solution.maxProfit(prices1)
    assert result1 == answer1, f"Expected {answer1}, but got {result1}"

    # Test case 2
    prices2 = [7,6,4,3,1]
    answer2 = 0
    result2 = solution.maxProfit(prices2)
    assert result2 == answer2, f"Expected {answer2}, but got {result2}"

    # Test case 3
    prices3 = [1]
    answer3 = 0
    result3 = solution.maxProfit(prices3)
    assert result3 == answer3, f"Expected {answer3}, but got {result3}"

    # Test case 4
    prices4 = [7,2,5,3,1,6,4]
    answer4 = 5
    result4 = solution.maxProfit(prices4)
    assert result4 == answer4, f"Expected {answer4}, but got {result4}"

    # Test case 5
    prices5 = [7,2,7,3,1,6,4]
    answer5 = 5
    result5 = solution.maxProfit(prices5)
    assert result5 == answer5, f"Expected {answer5}, but got {result5}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_maxProfit()
