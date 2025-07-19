# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findNode(root, v):
    if root == None:
        return False
    
    if root.val == v:
        return True

    l = findNode(root.left, v)
    r = findNode(root.right, v)

    return l or r

def findLCA(root, p, q):

    if root == None or root.val == p.val or root.val == q.val:
        return root

    left = findLCA(root.left, p, q)
    right = findLCA(root.right, p, q)

    if left and right:
        return root

    return left if left else right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        return findLCA(root, p, q)
