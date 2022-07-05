from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time limit exceeded
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        answer = ListNode()
        answer.next = ListNode()
        answerHead = answer.next

        carryOver = 0
        while l1 != None and l2 != None:
            answer = answer.next
            sum = l1.val + l2.val
            answer.val = sum % 10 + carryOver

            carryOver = sum // 10
            answer.next = ListNode()

            l1 = l1.next
            l2 = l2.next

        remaining = l1 if l1 != None else l2
        while remaining != None or carryOver != 0:
            answer = answer.next
            sum = (remaining.val if remaining != None else 0) + carryOver
            answer.val = sum % 10

            carryOver = sum // 10
            answer.next = ListNode()

        answer.next = None
        return answerHead
