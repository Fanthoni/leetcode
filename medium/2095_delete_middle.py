from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return None
        
        node_count = 1
        pointer = head

        while (pointer.next):
            pointer = pointer.next
            node_count += 1
        
        pointer = head

        for i in range(node_count // 2 - 1):
            pointer = pointer.next
            
        if (pointer.next.next != None):
            pointer.next = pointer.next.next
        else:
            pointer.next = None
        return head
