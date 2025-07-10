# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check(root):
    if not root:
        return 0

    right = check(root.right)
    if right == -1:
        return -1

    left = check(root.left)
    if left == -1:
        return -1

    if abs(right - left) > 1:
        return -1

    return 1 + max(left, right)
    


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return check(root) != -1
