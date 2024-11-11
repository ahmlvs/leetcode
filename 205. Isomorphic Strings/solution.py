# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s_map = {}
        # t_map = {}

        # for char in s:
        #     s_map[char] = s_map.get(char, 0) + 1
        
        # s_list = sorted(s_map.values())
        
        # for char in t:
        #     t_map[char] = t_map.get(char, 0) + 1
        
        # t_list = sorted(t_map.values())

        # if s_list == t_list:
        #     return True
        # else:
        #     return False
        # ## all this not corect
        # ## "bbbaaaba", "aaabbbba" need to be false

        s_map = {}
        t_map = {}

        # zip s ant t to (char_s, char_t)
        for char_s, char_t in zip(s, t):
            # we check that char_s and char_t in maps
            # and that char_s -> char_t in s_map
            # and that char_t -> char_s in t_map
            if (char_s in s_map and s_map[char_s] != char_t) or (char_t in t_map and t_map[char_t] != char_s):
                return False
            
            # save that for ind=1
            # for example
            # s_map = {'e': 'a'}
            # t_map = {'a': 'e'}
            s_map[char_s] = char_t
            t_map[char_t] = char_s
        
        return True
