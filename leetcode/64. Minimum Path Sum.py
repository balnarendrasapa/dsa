class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in i] for i in grid]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue

                m1 = 999999
                if i - 1 >= 0:
                    m1 = dp[i-1][j]

                m2 = 999999
                if j - 1 >= 0:
                    m2 = dp[i][j-1]

                # m3 = 99999999
                # if i - 1 >= 0 and j - 1 >= 0:
                #     m3 = dp[i-1][j-1]

                dp[i][j] = min(m1, m2) + grid[i][j]
        
        return dp[-1][-1]
