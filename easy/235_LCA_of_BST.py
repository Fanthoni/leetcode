# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Failed
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', pRoute=[], qRoute=[]) -> 'TreeNode':
        pRoute.append(root) if len(pRoute) == 0 or pRoute[-1] != p else None
        qRoute.append(root) if len(qRoute) == 0 or qRoute[-1] != q else None

        if pRoute[-1] == p and qRoute[-1] == q:
            filter(lambda route: route in qRoute, pRoute)
            return pRoute[-1]

        fromLeft = self.lowestCommonAncestor(
            root.left, p, q, pRoute, qRoute) if root.left else None

        if fromLeft != None:
            return fromLeft

        fromRight = self.lowestCommonAncestor(
            root.right, p, q, pRoute, qRoute) if root.right else None
        if fromRight != None:
            return fromRight

        pRoute.remove(root) if root in pRoute else None
        qRoute.remove(root) if root in qRoute else None

        return None
