from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Successs
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        Q = [root]
        res = []

        while len(Q) > 0:

            currLevelOrder = []
            nextQ = []

            while len(Q) > 0:
                node = Q.pop(0)

                currLevelOrder.append(node.val)
                if node.left != None:
                    nextQ.append(node.left)
                if node.right != None:
                    nextQ.append(node.right)

            Q.extend(nextQ)
            nextQ.clear()
            res.append(currLevelOrder)

        return res


testData = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().levelOrder(testData))
