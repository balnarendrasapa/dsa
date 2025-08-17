# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafs(self, root, l):
        if not root:
            return l
        
        if root and not root.left and not root.right:
            l += [root.val]
            return l

        left = self.getLeafs(root.left, l)
        right = self.getLeafs(root.right, left)

        return right

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = self.getLeafs(root1, [])
        r2 = self.getLeafs(root2, [])

        if len(r1) != len(r2):
            return False

        for i in range(len(r1)):
            if r1[i] != r2[i]:
                return False


        return True
