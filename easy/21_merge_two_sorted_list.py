from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Success
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        answerHead = answer

        while list1 != None and list2 != None:
            # smallerVal = list1.val if list1.val <= list2.val else list2.val
            # if list1 != None and list2 != None:
            if list1.val <= list2.val:
                smallerVal = list1.val
                list1 = list1.next
            else:
                smallerVal = list2.val
                list2 = list2.next
            # else:
            #     smallerVal = list1.val if list1 != None else list2.val

            answer.next = ListNode(smallerVal)
            answer = answer.next

        answer.next = list1 if list1 != None else list2

        return answerHead.next
