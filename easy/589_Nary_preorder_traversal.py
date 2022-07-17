from typing import List

"""
# Definition for a Node.


"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # Success
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        self.traverse(root, res)

        return res

    def traverse(self, root: 'Node', order: List[int]) -> List[int]:
        if not root:
            return

        order.append(root.val)
        for child in root.children:
            self.traverse(child, order)
