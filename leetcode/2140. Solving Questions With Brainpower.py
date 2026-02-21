class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, power = questions[i]

            skip = dp[i + 1]

            solve = points
            next_idx = i + power + 1
            if next_idx < n:
                solve += dp[next_idx]

            dp[i] = max(skip, solve)

        return max(dp)
