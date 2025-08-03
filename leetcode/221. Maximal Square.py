class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        dp = [[0 for _ in matrix[0]] for _ in matrix]

        max_size = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                    max_size = max(max_size, dp[i][j])

        return max_size * max_size
