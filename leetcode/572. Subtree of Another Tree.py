# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSubtreeT(root, subroot):
    if not root:
        return False

    if isSameTree(root, subroot):
        return True

    return isSubtreeT(root.left, subroot) or isSubtreeT(root.right, subroot)

def isSameTree(root, subroot):
    if not root and not subroot:
        return True
    
    if not root or not subroot:
        return False
    
    if root.val != subroot.val:
        return False

    return isSameTree(root.left, subroot.left) and isSameTree(root.right, subroot.right)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return isSubtreeT(root, subRoot)
