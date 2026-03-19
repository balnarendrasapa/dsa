class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0
        n = len(grid[0])

        X, Y = [0] * n, [0] * n

        for row in grid:
            rowX = 0
            rowY = 0
            for j in range(n):

                rowX += (row[j] == "X")
                rowY += (row[j] == "Y")

                X[j] += rowX
                Y[j] += rowY

                ans += (X[j] > 0) & (X[j] == Y[j])

        return ans
