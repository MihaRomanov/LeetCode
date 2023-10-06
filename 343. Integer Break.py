# https://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            sum1 = 1
            while n > 4:
                sum1 *= 3
                n -= 3
            sum1 *=n
            return sum1