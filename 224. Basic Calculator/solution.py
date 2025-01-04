# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.


# help func to evaluate_stack
def evaluate_stack(stack):
    res = 0
    # sign {1, -1} of numbers
    sign = 1
    while stack:
        token = stack.pop()
        if isinstance(token, int):
            res += sign * token
        elif token == "+":
            sign = 1
        elif token == "-":
            sign = -1
    return res


class Solution:
    def calculate(self, s: str) -> int:
        # main stack
        stack = []
        # num to create multidigit numbers like "12"
        num = 0
        # flag to understand that we create num
        has_number = False

        for char in s:
            if char.isdigit():
                # cont create num
                num = num * 10 + int(char)
                has_number = True
            elif char in "+-":
                # if we are in creation num
                # put it in stack
                if has_number:
                    stack.append(num)
                    num = 0
                    has_number = False
                stack.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                # if we are in creation num
                # put it in stack
                if has_number:
                    stack.append(num)
                    num = 0
                    has_number = False
                
                # then need to create temp_stack for (...)
                # evaluate it and put it in main stack
                temp_stack = []
                while stack and stack[-1] != "(":
                    # right order for evaluation
                    temp_stack.append(stack.pop())
                # remove "(" from main stack
                stack.pop()
                stack.append(evaluate_stack(temp_stack))
        
        # if we are in creation num
        # put it in stack
        if has_number:
            stack.append(num)
        
        # return main stack evaluation
        # before need to reverse stack
        # because 1 + 2 - 3 not equal 3 - 2 + 1
        return evaluate_stack(stack[::-1])
