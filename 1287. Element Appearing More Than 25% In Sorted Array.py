# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return statistics.mode(arr)