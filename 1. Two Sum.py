#class Solution:
#    def twoSum(self, nums, target):
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                sum = nums[i] + nums[j]
#                if sum == target:
#                    return (i, j)

#p= Solution()
#print(p.twoSum([3,2,4],6))
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = j
            print(hashmap)

p = Solution()
print(p.twoSum([3,2,4],6))
