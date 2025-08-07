# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, l):
        if not root:
            return l
        
        if root.left:
            self.inorder(root.left, l)

        l.append(root.val)

        if root.right:
            self.inorder(root.right, l)

        return l

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root, [])
            
