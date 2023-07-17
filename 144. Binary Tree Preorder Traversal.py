# class Solution(object):
#     def preorderTraversal(self, root):
#         result = []
#         for i in root and not null:
#             result.append(i)
#             print(result)
#         return print(result)
my_list = [1, 2, 3, 4, 5]
last = my_list.pop()
print(last)

#
# p1= Solution()
# x = [1,2,null,3]
# p1.preorderTraversal(x)

class Solution(object):
    def preorderTraversal(self, root):
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
