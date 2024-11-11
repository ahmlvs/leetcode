# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for char_s in s:
            s_map[char_s] = s_map.get(char_s, 0) + 1

        for char_t in t:
            t_map[char_t] = t_map.get(char_t, 0) + 1
        
        return s_map == t_map

        ## use Counter
        # from collections import Counter
        # return Counter(s) == Counter(t)
