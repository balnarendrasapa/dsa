class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        m, n = len(points), len(points[0])
        dp = points[0][:]

        for i in range(1, m):
            best_so_far = float('-inf')
            left_max = [0] * n
            for j in range(n):
                best_so_far = max(best_so_far, dp[j] + j)
                left_max[j] = best_so_far - j

            best_so_far = float('-inf')
            right_max = [0] * n
            for j in range(n - 1, -1, -1):
                best_so_far = max(best_so_far, dp[j] - j)
                right_max[j] = best_so_far + j

            new_dp = [0] * n
            for j in range(n):
                best_prev = max(left_max[j], right_max[j])
                new_dp[j] = points[i][j] + best_prev

            dp = new_dp

        return max(dp)
