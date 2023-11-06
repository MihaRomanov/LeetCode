# https://leetcode.com/problems/extra-characters-in-a-string/description/
class Solution(object):
    def minExtraChar(self, s, dictionary):
        words = set(dictionary)
        n = len(s)
        f = [0]
        for i, char in enumerate(s):
            f.append(f[-1] + 1)
            for j in range(i + 1):
                if s[j: i + 1] in words:
                    f[-1] = min(f[-1], f[j])

        return f[-1]