from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        not_capture = set()

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            not_capture.add((i, j))

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < m and 0 <= ny < n and 
                        board[nx][ny] == 'O' and (nx, ny) not in not_capture):
                        not_capture.add((nx, ny))
                        queue.append((nx, ny))

        # Start BFS from all border 'O's
        for i in range(m):
            for j in range(n):
                if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == 'O':
                    if (i, j) not in not_capture:
                        bfs(i, j)

        # Flip all remaining 'O' to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in not_capture:
                    board[i][j] = 'X'
