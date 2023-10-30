# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/


class Solution(object):
    def sortByBits(self, arr):
        def popcount(n):  # Time: O(logn) ~= O(1) if n is a 32-bit number
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result

        arr.sort(key=lambda x: (popcount(x), x))
        return arr