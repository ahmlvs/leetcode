# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "(*)"
# Output: true
# Example 3:

# Input: s = "(*))"
# Output: true
 

# Constraints:

# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        balance = 0
        # from left to right
        for i in range(n):
            balance += -1 if s[i] == ")" else 1
            if balance < 0:
                return False
        
        balance = 0
        # from right to left
        for i in range(n-1, -1, -1):
            balance += -1 if s[i] == "(" else 1
            if balance < 0:
                return False
        
        return True
