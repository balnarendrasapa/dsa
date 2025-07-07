# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def good_nodes(root, max_v):
    if not root:
        return 0

    count = 1 if root.val >= max_v else 0
        
    max_v = max(max_v, root.val)
    count += good_nodes(root.left, max_v) 
    count += good_nodes(root.right, max_v) 

    return count

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return good_nodes(root, root.val)
