class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if j == 0 and j != n - 1:
                        min_array = [dp[i - 1][j], dp[i - 1][j + 1]]
                    elif j == n - 1:
                        min_array = [dp[i - 1][j - 1], dp[i - 1][j]]
                    else:
                        min_array = [dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]]

                    dp[i][j] = matrix[i][j] + min(min_array)

        return min(dp[-1])
