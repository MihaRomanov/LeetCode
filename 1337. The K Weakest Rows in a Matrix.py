#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/


class Solution:
    def kWeakestRows(self, mat: [int], k: int):
        power = []
        for r, row in enumerate(mat):
            tmp = 0
            for n in row:
                if n:
                    tmp += 1
                else:
                    break
            power.append((tmp, r))
        heapq.heapify(power)
        return [heapq.heappop(power)[1] for _ in range(k)]