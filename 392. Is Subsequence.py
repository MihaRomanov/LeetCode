# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        j = 0
        for i in range(m):
            if j < n and s[j] == t[i]:
                j += 1
        return j == n

