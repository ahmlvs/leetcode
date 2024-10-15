# test_best_time_to_buy_and_sell_stock.py

from best_time_to_buy_and_sell_stock import Solution

def test_solution():
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
    answer5 = 4
    result5 = solution.maxProfit(prices5)
    assert result5 == answer5, f"Expected {answer5}, but got {result5}"

    print("All test cases passed!")
