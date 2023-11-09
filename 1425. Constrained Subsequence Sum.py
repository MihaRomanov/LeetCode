# https://leetcode.com/problems/constrained-subsequence-sum/description/


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = nums[0]
        Dp = [0]*len(nums)
        Dp[0] = max(0,nums[0])
        DQ = collections.deque([0])

        for i in range(1, len(nums)):
            while(len(DQ) > 0 and i - DQ[0] > k):
                DQ.popleft()