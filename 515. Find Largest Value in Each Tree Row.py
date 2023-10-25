# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        def dfs(node, level, valList):
            if not node: return

            if level >= len(maxValInLevel):
                maxValInLevel.append(node.val)
            else:
                valList[level] = max(valList[level], node.val)

            if node.left:
                dfs(node.left, level + 1, valList)
            if node.right:
                dfs(node.right, level + 1, valList)

        maxValInLevel = []
        dfs(root, 0, maxValInLevel)

        return maxValInLevel