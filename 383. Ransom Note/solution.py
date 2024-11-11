# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # hashmap for magazine letters
        m = {}

        for char in magazine:
            # if char in m:
            #     m[char] += 1
            # else:
            #     m[char] = 1
            m[char] = m.get(char, 0) + 1
        
        for char in ransomNote:
            # if char not in m:
            #     return False
            # elif m[char] == 0:
            #     return False
            # else:
            #     m[char] -= 1
            if m.get(char, 0) == 0:
                return False
            else:
                m[char] -= 1
        
        return True
