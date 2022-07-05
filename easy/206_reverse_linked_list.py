from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Success
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        currNode = None
        prevNode = None

        while head != None:
            currNode = ListNode(head.val)
            currNode.next = prevNode

            prevNode = currNode
            head = head.next
        return currNode
