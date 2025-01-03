# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq = Counter(t)
        # number of unique chars in t
        required = len(t_freq)

        # window
        left = 0
        right = 0
        window_freq = {}
        # number of chars with required frequency in window
        formed = 0
        min_lenght = float("inf")
        min_window = (0, 0)

        # expand window to right
        # then try to minimize with left move
        while right < len(s):
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1

            # check if char meets req in t
            if char in t_freq and window_freq[char] == t_freq[char]:
                formed += 1
            
            # move left if we can
            while left <= right and formed == required:
                left_char = s[left]

                # update smallest window if neccesary
                if right - left + 1 < min_lenght:
                    min_lenght = right - left + 1
                    min_window = (left, right)
                
                # change window freq and move left
                window_freq[left_char] -= 1
                if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if min_lenght == float("inf") else s[min_window[0]:min_window[1] + 1]
