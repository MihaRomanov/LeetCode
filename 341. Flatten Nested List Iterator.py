# https://leetcode.com/problems/flatten-nested-list-iterator/description/

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.q = []
        self.flatten(nestedList)

    def flatten(self, nl):
        for i in nl:
            if i.isInteger():
                self.q.append(i.getInteger())

            else:
                self.flatten(i.getList())

    def next(self) -> int:
        return self.q.pop(0)

    def hasNext(self) -> bool:
        return True if self.q else False