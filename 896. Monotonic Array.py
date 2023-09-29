# https://leetcode.com/problems/monotonic-array/
class Solution:
    class Solution:
        def isMonotonic(self, nums: List[int]) -> bool:
            increasing = True
            decreasing = True

            for i in range(1, len(nums)):
                increasing &= nums[i - 1] <= nums[i]
                decreasing &= nums[i - 1] >= nums[i]

            return increasing or decreasing


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        direction = 0  # 0 means unknown, 1 means increasing, -1 means decreasing

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # increasing
                if direction == 0:
                    direction = 1
                elif direction == -1:
                    return False
            elif nums[i] < nums[i - 1]:  # decreasing
                if direction == 0:
                    direction = -1
                elif direction == 1:
                    return False

        return True