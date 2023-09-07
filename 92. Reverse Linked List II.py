#https://leetcode.com/problems/reverse-linked-list-ii/

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        fake = ListNode(0, head)

        leftPrev, cur = fake, head
        for i in range(left-1):
            leftPrev, cur = cur, cur.next

        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext
        leftPrev.next.next = cur
        leftPrev.next = prev
        return fake.next

