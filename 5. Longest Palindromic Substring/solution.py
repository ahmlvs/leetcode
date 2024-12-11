# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n < 2:
            return s
        
        # dp[i][j] is True if s[i:j+1] palindrome
        dp = [[False] * n for _ in range(n)]

        # "a" one char substrings are palindrome
        for i in range(n):
            dp[i][i] = True
        
        # start index and lenght for result
        start, max_length = 0, 1

        # firstly check 2 chars substrings
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
        
        # next check >2 chars substrings
        for length in range(3, n+1):
            for i in range(n - length + 1):
                # end of substring
                j = i + length - 1
                # if s[i] == s[j]
                # and middle substring is palindrome
                # so s[i] + middle + s[j] also palindrome
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        return s[start:start + max_length]
