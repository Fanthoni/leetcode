from types import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if (root == None):
            return []

        Q = [root]
        row_array = []
        curr_row_values = []

        while (len(Q) > 0):
            curr_node = Q[0]

            if (curr_node != "N"):
                curr_row_values.append(curr_node.val)

                if (curr_node.right or curr_node.left):
                    if ("N") not in Q:
                        Q.append("N")
                    if (curr_node.right):
                        Q.append(curr_node.right)
                    if (curr_node.left):
                        Q.append(curr_node.left)
            else:
                row_array.append(curr_row_values)
                curr_row_values = []

            Q.pop(0)

        if (curr_row_values):
            row_array.append(curr_row_values)

        res = [max(row) for row in row_array]
        return res
