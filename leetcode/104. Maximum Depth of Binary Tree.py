# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root, depth = 0):

    if root == None:
        return depth

    depth_left = inorder(root.left, depth + 1)
    depth_right = inorder(root.right, depth + 1)

    return max(depth_left, depth_right, depth)
    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return inorder(root)
