# https://leetcode.com/problems/power-of-four/description/

class Solution:
    def isPowerOfFour(self, num):
        return num != 0 and num &(num-1) == 0 and num & 0x55555555== num