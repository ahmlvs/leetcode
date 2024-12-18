# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s, opened, closed):
            # print(s, opened, closed)
            # finally 2n ()
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # if we can we add one more (
            if opened < n:
                backtrack(s + "(", opened + 1, closed)
            
            # if we can close opened ( we add )
            if closed < opened:
                backtrack(s + ")", opened, closed + 1)
        
        backtrack("", 0, 0)
        return result
