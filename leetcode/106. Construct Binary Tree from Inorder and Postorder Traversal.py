# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            if postorder[-1] not in inorder:
                postorder = postorder[:-1]
                root = self.buildTree(inorder, postorder)
            else:
                index = inorder.index(postorder[-1])
                postorder = postorder[:-1]
                root = TreeNode(inorder[index])
                root.left = self.buildTree(inorder[:index], postorder)
                root.right = self.buildTree(inorder[index+1:], postorder)

            return root
