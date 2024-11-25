# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # array of rows strings
        result = [""] * numRows
        # next row direction
        if numRows == 1:
            move_y = 0
        else:
            move_y = -1
        current_row = 0

        for char in s:
            # add char to right row
            result[current_row] += char

            # if 0 or last row need to chage direction
            if current_row == 0 or current_row == numRows - 1:
                move_y *= -1

            # move to next row
            current_row += move_y
        
        return "".join(result)
