# lc876: middle of linked list
# see: https://leetcode.com/problems/middle-of-the-linked-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use two pointers
        # second pointer jumps two steps
        # 1->2->null, therefore, middle is second
        # 1->null, return head
        # 1->2->3->null , second ptr sees null, return first ptr
        if not head.next:
            return head

        if not head.next.next:
            return head.next

        p1, p2 = head, head
        while p2:
            if not p2.next:
                return p1
            elif not p2.next.next:
                return p1.next
                
            p1 = p1.next
            p2 = p2.next.next
        return p1

if __name__ == "__main__":
    s = Solution()
    # [1,2,3,4,5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    r = s.middleNode(head)

    while r:
        print(r.val)
        r = r.next
