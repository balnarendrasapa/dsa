import heapq

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        er, ec = entrance[0], entrance[1]
        heap = [(0, er, ec)]

        m = len(maze)
        n = len(maze[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[er][ec] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while heap:
            steps, x, y = heapq.heappop(heap)
            
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and (x != er or y != ec):
                return steps

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == ".":
                    visited[nx][ny] = True
                    heapq.heappush(heap, (steps + 1, nx, ny))

        return -1
