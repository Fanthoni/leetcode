from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Success
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lengthOfList = 0
        explorer = head
        nextOfRemoved = None

        while explorer != None:
            explorer = explorer.next
            lengthOfList += 1

        if lengthOfList == 1 and n == 1:
            return None

        if n == lengthOfList:
            return head.next

        fast = slow = headOfAnswer = head

        for i in range(lengthOfList - n - 1):
            fast, slow = fast.next, slow.next

        nextOfRemoved = fast.next.next if fast.next != None else None
        slow.next = nextOfRemoved
        return headOfAnswer
