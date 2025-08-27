class Solution:
    def find(self, grid, i, j, d, allowed, target):
        ni = i + self.directions[d][0]
        nj = j + self.directions[d][1]

        if ni >= len(grid) or nj >= len(grid[0]) or ni < 0 or nj < 0 or grid[ni][nj] != target:
            return 0

        nottake = 1 + self.dp(ni, nj, d, allowed, 2 - target)
        take = 0
        if allowed:
            take = 1 + self.dp(ni, nj, (d + 1) % 4, False, 2 - target)

        return max(nottake, take)

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        result = 0

        @lru_cache(None)
        def dp(i, j, d, allowed, target):
            return self.find(grid, i, j, d, allowed, target)

        self.dp = dp

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d in range(4):
                        result = max(
                            result,
                            1 + self.dp(i, j, d, True, 2)
                        )

        return result
