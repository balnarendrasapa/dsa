# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def inorder(root, path, sum_v):
            if not root:
                return

            path.append(root.val)
            sum_v += root.val

            if not root.left and not root.right and sum_v == targetSum:
                result.append(path[:])

            inorder(root.left, path, sum_v)
            inorder(root.right, path, sum_v)

            path.pop()

        inorder(root, [], 0)
        return result
