from typing import Optional
from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # # O(N) time and memory
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     heap = []
    #     heapify(heap)
    #     curr = head

    #     while curr is not None:
    #         heappush(heap, curr.val)
    #         curr = curr.next
    #     sorted = [heappop(heap) for i in range(len(heap))]

    #     currHead = curr = head
    #     for i in range(len(sorted)):
    #         curr.val = sorted[i]
    #         curr = curr.next

    #     return currHead

    # O(n log n) time and O(1) memory
    # Divide and conquer - Merge Sort
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head.next is None):
            return head

        # Find the middle of the list
        slowP = fastP = head
        while (fastP is not None and fastP.next is not None):
            slowP = slowP.next
            fastP = fastP.next.next

        tailOfLeft = head
        while (tailOfLeft.next is not slowP):
            tailOfLeft = tailOfLeft.next
        tailOfLeft.next = None

        leftSorted, rightSorted = self.sortList(head), self.sortList(slowP)
        return self.merge(leftSorted, rightSorted)

    # Merge two sorted linked list

    def merge(self, leftHead, rightHead):
        sorted = sortedHead = ListNode()

        while (leftHead is not None and rightHead is not None):
            if leftHead.val < rightHead.val:
                sorted.next = ListNode(leftHead.val)
                leftHead = leftHead.next
            else:
                sorted.val = rightHead.val
                sorted.next = ListNode(rightHead.val)
            sorted = sorted.next

        if leftHead is not None:
            sorted.next = leftHead
        else:
            sorted.next = rightHead

        return sortedHead
