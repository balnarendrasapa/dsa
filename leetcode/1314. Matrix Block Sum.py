class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(mat[0])
        m = len(mat)

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i - 1][j]

                if j > 0:
                    dp[i][j] += dp[i][j - 1]

                if i > 0 and j > 0:
                    dp[i][j] -= dp[i - 1][j - 1]

                dp[i][j] += mat[i][j]

        result = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)

                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)
                
                total = dp[r2][c2]
                if r1 > 0:
                    total -= dp[r1 - 1][c2]

                if c1 > 0:
                    total -= dp[r2][c1 - 1]

                if r1 > 0 and c1 > 0:
                    total += dp[r1 - 1][c1 - 1]

                result[i][j] = total

        return result
