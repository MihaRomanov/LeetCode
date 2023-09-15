#https://leetcode.com/problems/maximum-ice-cream-bars/description/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            coins -= costs[i]  # Buy the ith iceream
            if coins < 0:  # check if we can afford more
                return i
        # if we bought all icecreams and still got coins
        return len(costs)