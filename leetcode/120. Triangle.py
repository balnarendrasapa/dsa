class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [[0 for _ in i] for i in triangle]

        for index in range(len(triangle)):
            if index == 0:
                dp[0][0] = triangle[0][0]
                continue

            length = len(triangle[index])

            for j in range(length):
                m1 = 9999
                if j - 1 >= 0:
                    m1 = dp[index - 1][j - 1]

                m2 = 9999
                if j < length - 1:
                    m2 = dp[index - 1][j]

                dp[index][j] = min(m1, m2) + triangle[index][j]

        return min(dp[-1])
