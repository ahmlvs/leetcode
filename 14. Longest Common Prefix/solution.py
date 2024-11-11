# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # let's set prefix like first string
        prefix = strs[0]

        # iterate throught next strings
        # and find LCP near two next strings
        for s in strs[1:]:
            # while prefix no ""
            # we check all prefixes and actual prefix
            while prefix and s[:len(prefix)] != prefix:
                prefix = prefix[:-1]

            # if prefix is ""
            # there not LCP
            if prefix == "":
                return ""
        
        return prefix
