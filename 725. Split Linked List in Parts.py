# https://leetcode.com/problems/split-linked-list-in-parts/
# class Solution:
#     def splitListToParts(self, head, k):
#         count_parts = round(len(head)/k)
#
#         print(count_parts)
#         return count_parts
#
# sol = Solution()
# sol.splitListToParts([1,2,3,4,5,6,7,8,9,10], k = 3)

class Solution:
  def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
    ans = [[] for _ in range(k)]
    length = 0
    curr = root
    while curr:
      length += 1
      curr = curr.next
    subLength = length // k
    remainder = length % k

    prev = None
    head = root

    for i in range(k):
      ans[i] = head
      for j in range(subLength + (1 if remainder > 0 else 0)):
        prev = head
        head = head.next
      if prev:
        prev.next = None
      remainder -= 1

    return ans
