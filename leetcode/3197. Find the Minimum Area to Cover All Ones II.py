class Solution:
    def rotate(self, grid):
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        res = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                res[m - j - 1][i] = grid[i][j]

        return res

    def minSum(self, grid, u, d, l, r):
        min_i = len(grid)
        min_j = len(grid[0])
        max_i = 0
        max_j = 0

        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)

        return (
            (max_i - min_i + 1) * (max_j - min_j + 1)
            if min_i <= max_i
            else sys.maxsize // 3
        )

    def solve(self, grid):
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        res = n * m

        for i in range(n - 1):
            for j in range(m - 1):
                res = min(
                    res,
                    self.minSum(grid, 0, i, 0, m - 1) +
                    self.minSum(grid, i + 1, n - 1, 0, j) +
                    self.minSum(grid, i + 1, n - 1, j + 1, m - 1)
                )

                res = min(
                    res,
                    self.minSum(grid, 0, i, 0, j) + 
                    self.minSum(grid, 0, i, j + 1, m - 1) + 
                    self.minSum(grid, i + 1, n - 1, 0, m - 1)
                )

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                res = min(
                    res,
                    self.minSum(grid, 0, i, 0, m - 1) + 
                    self.minSum(grid, i + 1, j, 0, m - 1) + 
                    self.minSum(grid, j + 1, n - 1, 0, m - 1)
                )

        return res

    def minimumSum(self, grid: List[List[int]]) -> int:
        anti_clockwise = self.rotate(grid)
        return min(self.solve(grid), self.solve(anti_clockwise))
