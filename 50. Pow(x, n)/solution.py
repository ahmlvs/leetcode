# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x ** n

        # if x == 0:
        #     return 0
        
        # if n == 0:
        #     return 1
        
        # if n > 0:
        #     exp = n
        #     base = x
        # else:
        #     exp = -n
        #     base = 1 / x
        
        # result = 1
        
        # for i in range(1,exp+1):
        #     result *= base
        
        # return result

        # but this solution gives TLE for
        # x = 0.00001 and n = 2147483647

        ## fast pow
        def fastPow(base, exp):
            if exp == 0:
                return 1.0
            
            # if exp even
            # exp = exp/2 + exp/2
            # if oven
            # exp = exp/2 + exp/2 + 1
            half = fastPow(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            x = 1 / x
            n = -n
        
        return fastPow(x, n)
