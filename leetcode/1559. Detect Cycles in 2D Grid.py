class Solution:

    def dfs(self, grid, dp, x, y, prev):
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dp[x][y] = True

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not dp[nx][ny] and grid[nx][ny] == grid[x][y]:
                    if self.dfs(grid, dp, nx, ny, (x, y)):
                        return True
                elif dp[nx][ny] and grid[nx][ny] == grid[x][y] and prev != (nx, ny):
                    return True

        return False



    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        dp = [[False for _ in range(n)] for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if not dp[x][y]:
                    if self.dfs(grid, dp, x, y, (None, None)):
                        return True

        return False

