# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        total_swaps = 0
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

            total_swaps += self.min_swaps(level)

        return total_swaps

    def min_swaps(self, arr):
        n = len(arr)
        pairs = [(arr[i], i) for i in range(n)]
        pairs.sort()

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pairs[i][1] == i:
                continue

            j = i
            cycle_size = 0
            while not visited[j]:
                visited[j] = True
                j = pairs[j][1]
                cycle_size += 1
            
            swaps += cycle_size - 1

        return swaps

        
