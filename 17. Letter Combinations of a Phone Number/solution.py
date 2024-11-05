# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []

        # for "23"
        # index=0 -> 2 -> path=["a"] + backtrack for next index
        # then path=["b"] + backtrack for next index

        def backtrack(index, path):
            # if index == len(digits) need to stop
            if index == len(digits):
                result.append("".join(path))
                return
            
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # add letter to path
                # and call backtrack next index
                path.append(letter)
                backtrack(index+1, path)
                # delete last letter from path
                path.pop()
        
        # start from 0 index of digits
        # and nothing in path
        backtrack(0, [])
        return result
