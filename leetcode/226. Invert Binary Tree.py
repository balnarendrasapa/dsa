# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(root):
    if root == None:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp

    invert(root.left)
    invert(root.right)

    return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return invert(root)
