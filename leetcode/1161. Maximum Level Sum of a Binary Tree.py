# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        level = 0
        max_tracker = float("-inf")
        max_level = 0

        while que:
            level_size = len(que)
            level += 1
            s = 0

            for i in range(level_size):
                node = que.popleft()

                s += node.val

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)

            if max_tracker < s:
                max_tracker = s
                max_level = level

        return max_level
