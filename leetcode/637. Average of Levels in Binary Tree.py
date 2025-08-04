# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([root])
        averages = []

        while que:
            level_size = len(que)
            average = 0

            for _ in range(level_size):
                node = que.popleft()

                average += node.val

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

            averages.append(average / level_size)


        return averages
