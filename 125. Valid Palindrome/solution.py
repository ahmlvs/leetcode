# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean s to only letters and numbers
        # with .isalnum()
        # make all chars .lower()
        cleaned_s = "".join([char.lower() for char in s if char.isalnum()])

        # 2 pointers
        # check from left and right side
        left = 0
        right = len(cleaned_s) - 1

        while left < right:
            if cleaned_s[left] == cleaned_s[right]:
                # if == move to next
                left += 1
                right -= 1
            else:
                # it is not palindrome
                return False

        return True
