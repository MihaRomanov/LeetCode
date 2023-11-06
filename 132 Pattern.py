# https://leetcode.com/problems/132-pattern/description/


class Solution(object):
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        curr_min = nums[0]
        for i in range(1, len(nums)-1):
            if curr_min < nums[i]:
                for j in range(i+1, len(nums)):
                    if curr_min < nums[j] < nums[i]:
                        return True
            else:
                curr_min = nums[i]
        return False