# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = deque([root])
        result = []

        flag = 0

        while que:
            level_size = len(que)
            level = []

            for _ in range(level_size):
                node = que.popleft()

                level.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if flag % 2 == 0:
                result.append(level)
            else:
                result.append(level[::-1])
            
            flag += 1

        return result
