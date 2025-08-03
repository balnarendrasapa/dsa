# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxvalue(root, mv):
    if root == None:
        return 0

    left = maxvalue(root.left, mv)
    right = maxvalue(root.right, mv)

    mv[0] = max(mv[0], root.val + left + right, root.val, root.val + left, root.val + right)

    return max(root.val, root.val + left, root.val + right)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mv = [-9999999]
        temp = maxvalue(root, mv)
        return mv[0]
