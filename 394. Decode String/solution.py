# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].


class Solution:
    def decodeString(self, s: str) -> str:
        # save substrings and num
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                # add to actual current_num
                current_num = current_num * 10 + int(char)
            # if "[" need to same current to stack 
            elif char == "[":
                stack.append((current_str, current_num))
                # add reset currents
                current_str = ""
                current_num = 0
            # if "]" need to pop last stack
            # and add to current
            elif char == "]":
                last_str, last_num = stack.pop()
                # last_num it is time of current str
                current_str = last_str + last_num * current_str
            # simply add char to current_str
            else:
                current_str += char
        
        return current_str
