# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi=""
        for i in range(0,len(num)-2):
            if len(set([num[i],num[i+1],num[i+2]]))==1:
                maxi=max(maxi,num[i])
        return maxi*3