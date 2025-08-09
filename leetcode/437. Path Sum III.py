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

    def pathSum(self, root, targetSum):
        if not root:
            return 0

        count_here = 0
        self.count = 0
        self.pathCounts(root, 0, targetSum)
        count_here += self.count

        count_here += self.pathSum(root.left, targetSum)
        count_here += self.pathSum(root.right, targetSum)

        return count_here
