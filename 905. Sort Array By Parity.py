# https://leetcode.com/problems/sort-array-by-parity/description/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            if nums[count]%2:
                nums.append(nums.pop(count))
            else:
                count +=1
        return nums

