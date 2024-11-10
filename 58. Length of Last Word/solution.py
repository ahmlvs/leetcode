# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s_strip = s.strip()
        # s_list = s_strip.split(" ")
        # return len(s_list[-1])

        n = len(s)
        length = 0
        in_word = False

        # start from back
        for i in range(n-1, -1, -1):
            if s[i] != " ":
                length += 1
                in_word = True
            elif in_word:
                # first " " after last word
                break
        
        return length
