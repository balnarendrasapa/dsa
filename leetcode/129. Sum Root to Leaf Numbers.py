# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getList(root, str_v, str_list):
    if not root:
        return []

    str_v += str(root.val)

    if not root.left and not root.right:
        return str_list + [str_v]

    left = getList(root.left, str_v, [])
    right = getList(root.right, str_v, [])

    return left + right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        l = getList(root, "", [])
        return sum(int(i) for i in l)
