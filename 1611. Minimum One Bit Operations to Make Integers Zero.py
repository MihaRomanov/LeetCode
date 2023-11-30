# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/


class Solution(object):
    def minimumOneBitOperations(self, n):
        if n <= 1:
            return n
        count = 0
        while (1 << count) <= n:
            count += 1
        return ((1 << count) - 1) - self.minimumOneBitOperations(n - (1 << (count - 1)))