class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
            
        dp = [[0 for i in obstacleGrid[0]] for j in obstacleGrid]
        dp[0][0] = 1

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j != 0 and obstacleGrid[i][j - 1] != 1:
                    dp[i][j] = dp[i][j - 1]
                elif i != 0 and j == 0 and obstacleGrid[i - 1][j] != 1:
                    dp[i][j] = dp[i - 1][j]
                
                if i != 0 and j != 0:
                    if obstacleGrid[i - 1][j] != 1:
                        dp[i][j] += dp[i - 1][j]

                    if obstacleGrid[i][j - 1] != 1:
                        dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]
