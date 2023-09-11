# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
#
# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example,
# if groupSizes[1] = 3, then person 1 must be in a group of size 3.
#
# Return a list of groups such that each person i is in a group of size groupSizes[i].
#
# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers,
# return any of them. It is guaranteed that there will be at least one valid solution for the given input.

import collections


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups, result = collections.defaultdict(list), []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups.pop(size))
        return result