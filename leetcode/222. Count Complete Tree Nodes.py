# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def countNodesN(root):
    if not root:
        return 0

    return 1 + countNodesN(root.left) + countNodesN(root.right)
    
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return countNodesN(root)
