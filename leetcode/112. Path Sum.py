def inorder(root, cS, tS):
    if root is None:
        return False

    cS += root.val

    if root.left is None and root.right is None:
        return cS == tS

    return inorder(root.left, cS, tS) or inorder(root.right, cS, tS)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return inorder(root, 0, targetSum)
