# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # base answer 0
        answer = [0] * n
        # to hold indexes
        stack = []

        for i in range(n):
            # while stack has el
            # and top temp in stack < actual
            # pop elements and create answer
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # some prev day index
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            # add this el to stack
            stack.append(i)
        
        return answer
