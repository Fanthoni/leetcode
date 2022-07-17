from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Success
    def isValidBST(self, root: Optional[TreeNode], maxCap=float('+inf'), minCap=float("-inf")) -> bool:
        if root == None:
            return True

        parentVal = root.val
        if (root.left != None and (root.left.val >= parentVal or root.left.val <= minCap)) \
                or (root.right != None and (root.right.val <= parentVal or root.right.val >= maxCap)):
            return False

        return self.isValidBST(root.left, min(maxCap, root.val), minCap) \
            and self.isValidBST(root.right, maxCap, max(minCap, root.val))
