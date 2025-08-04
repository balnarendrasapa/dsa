# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        que = deque([root])

        result = []

        while que:
            level_size = len(que)
            last = None

            for _ in range(level_size):
                node = que.popleft()

                last = node

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)

            result.append(last.val)

        return result
