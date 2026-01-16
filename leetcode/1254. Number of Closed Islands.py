class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = 1
            is_closed = True

            while q:

                x, y = q.popleft()

                if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                    is_closed = False

                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))

            return is_closed
        
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and bfs(i, j):
                    count += 1

        return count
