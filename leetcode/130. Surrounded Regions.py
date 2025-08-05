# from collections import deque
# from typing import List

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         if not board or not board[0]:
#             return

#         m, n = len(board), len(board[0])
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         not_capture = set()

#         def bfs(i, j):
#             queue = deque()
#             queue.append((i, j))
#             not_capture.add((i, j))

#             while queue:
#                 x, y = queue.popleft()
#                 for dx, dy in directions:
#                     nx, ny = x + dx, y + dy
#                     if (0 <= nx < m and 0 <= ny < n and 
#                         board[nx][ny] == 'O' and (nx, ny) not in not_capture):
#                         not_capture.add((nx, ny))
#                         queue.append((nx, ny))

#         # Start BFS from all border 'O's
#         for i in range(m):
#             for j in range(n):
#                 if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == 'O':
#                     if (i, j) not in not_capture:
#                         bfs(i, j)

#         # Flip all remaining 'O' to 'X'
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'O' and (i, j) not in not_capture:
#                     board[i][j] = 'X'

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        not_capture = []
        m = len(board)
        n = len(board[0])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def findadjacent(i, j):
            que = deque([[i, j]])

            while que:
                i, j = que.popleft()

                for dx, dy in directions:
                    if 0 <= i + dx < m and 0 <= j + dy < n and board[i + dx][j + dy] == "O" and [i + dx, j + dy] not in not_capture:
                        not_capture.append([i + dx, j + dy])
                        que.append([i + dx, j + dy])

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if board[i][j] == "O" and [i, j] not in not_capture:
                        not_capture.append([i, j])
                        findadjacent(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and [i, j] not in not_capture:
                    board[i][j] = "X"
        
