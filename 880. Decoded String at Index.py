# https://leetcode.com/problems/decoded-string-at-index/description/
class Solution:
    def decodeAtIndex(self, S, K):
        size=0
        for i in S:
            if(i.isdigit()):
                size*=int(i)
            else:
                size+=1
        for index in reversed(S):
            K %= size
            if(K==0 and index.isalpha()):
                return index
            if(index.isdigit()):
                size/=int(index)
            else:
                size-=1
        return