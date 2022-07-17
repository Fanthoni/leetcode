from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Success
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        p1, p2 = head, head

        if p1.next == None:
            return p1

        while True:
            p1 = p1.next
            p2 = p2.next

            if p2 == None:
                return p1

            p2 = p2.next
            if p2 == None or p2.next == None:
                return p1
