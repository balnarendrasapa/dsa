# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathCounts(self, root, parentSum, targetSum):
        if not root:
            return

        if parentSum + root.val == targetSum:
            self.count += 1

        self.pathCounts(root.left, parentSum + root.val, targetSum)
        self.pathCounts(root.right, parentSum + root.val, targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        self.count = 0
        self.pathCounts(root, 0, targetSum)

        self.count += self.pathSum(root.left, targetSum)
        self.count += self.pathSum(root.right, targetSum)

        return self.count
