"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
            
        que = deque([root])

        while que:
            level_size = len(que)
            prev = Node()

            for _ in range(level_size):
                node = que.popleft()

                prev.next = node

                prev = node

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

        return root
