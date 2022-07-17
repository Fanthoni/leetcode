from typing import Optional

"""
# Definition for a Node.

"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # Succss
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root

        Q = [root]
        nextQ = []

        while len(Q) != 0:

            # for node in Q:
            for i in range(len(Q)):
                node = Q[i]
                nextQ.append(node.left) if node.left != None else None
                nextQ.append(node.right) if node.right != None else None

                node.next = Q[i + 1] if i < len(Q) - 1 else None

            Q.clear()
            Q.extend(nextQ)
            nextQ.clear()

        return root
