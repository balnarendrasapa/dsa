# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findNode(root, node):
    if not root:
        return False
    
    a = findNode(root.left, node)

    if root is node:
        return True

    b = findNode(root.right, node)

    return a or b

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        temp = root
        while temp:
            if temp is p or temp is q:
                return temp

            check1 = findNode(temp.left, p)
            check2 = findNode(temp.left, q)
            check3 = findNode(temp.right, p)
            check4 = findNode(temp.right, q)

            if check1 and check2:
                temp = temp.left
            
            if check3 and check4:
                temp = temp.right

            if (check1 and check4) or (check2 and check3):
                return temp
