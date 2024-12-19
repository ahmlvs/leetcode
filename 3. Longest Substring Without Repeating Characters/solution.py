# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        # hashmap to hold chars indexes
        char_index = {}

        max_length = 0
        # 2 pointers for sliding window
        start = 0

        for end in range(n):
            char = s[end]

            # check is char in char_index
            # and char_index[char] >= start
            # if True move start on next pos
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            # update char_index[char] to last
            char_index[char] = end
            
            # update max_length
            max_length = max(max_length, end - start + 1)
    
        return max_length