class Solution:
    def check(self, r, c, opened, grid):
        m = len(grid)
        n = len(grid[0])

        if opened < 0:
            return False

        if r == m - 1 and c == n - 1:
            return True if opened == 0 else False

        if (r, c, opened) in self.memo:
            return self.memo[(r, c, opened)]

        ans = False
        if r + 1 < m:
            ans = ans or self.check(r + 1, c, opened + 1 if grid[r + 1][c] == "(" else opened - 1, grid)
        if c + 1 < n:
            ans = ans or self.check(r, c + 1, opened + 1 if grid[r][c + 1] == "(" else opened - 1, grid)
        
        self.memo[(r, c, opened)] = ans
        return ans
        
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        self.memo = {}
        return self.check(0, 0, 1 if grid[0][0] == "(" else -1, grid)
