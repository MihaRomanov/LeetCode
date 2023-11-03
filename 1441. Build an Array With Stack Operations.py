# https://leetcode.com/problems/build-an-array-with-stack-operations/description/


class Solution:
    def buildArray(self, target, n: int):
        res = []
        p = 0
        for i in range(1, n + 1):
            if target[p] == i:
                res.append("Push")
                p += 1
            else:
                res.append("Push")
                res.append("Pop")
            if p == len(target):
                break
        return res