# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1
 

# Constraints:

# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        left = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        
        for right in range(n):
            char_count[s[right]] += 1
            
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                ans += n - right
                char_count[s[left]] -= 1
                left += 1
        
        return ans
