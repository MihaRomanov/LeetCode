class Solution(object):
    def isSameTree(self, p, q):
        for i in p:
            for a in q:
                if i==a:
                    continue
                else:
                    return print(False)
        return print(True)

p = Solution()
p.isSameTree(p = [1,2,3], q = [1,2,3])
