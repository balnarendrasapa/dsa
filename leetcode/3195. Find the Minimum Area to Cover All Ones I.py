class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        min_i = m
        max_i = 0
        min_j = n
        max_j = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)

                    min_j = min(min_j, j)
                    max_j = max(max_j, j)

        return (max_i - min_i + 1) * (max_j - min_j + 1)
