# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false

 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        if len(pattern) != len(s_list):
            return False
        
        p_map = {}
        s_map = {}

        # zip pattern ant s_list to (p, word)
        for p, word in zip(pattern, s_list):
            # we check that p and word in maps
            # and that p -> word in p_map
            # and that word -> p in s_map
            if (p in p_map and p_map[p] != word) or (word in s_map and s_map[word] != p):
                return False
            
            # save that for ind=1
            # for example
            # p_map = {'a': 'dog'}
            # s_map = {'dog': 'a'}
            p_map[p] = word
            s_map[word] = p
        
        return True
        