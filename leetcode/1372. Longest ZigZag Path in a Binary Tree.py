# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root, left, right):
        self.max = max(self.max, right, left)

        if root.left:
            self.traverse(root.left, right + 1, 0)
        
        if root.right:
            self.traverse(root.right, 0, left + 1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.traverse(root, 0, 0)
        return self.max
        
