class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        # (prev_index, length)
        dp = [(-1, 1) for _ in range(n)]
        max_v = 1
        l = 0

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[j][1] + 1 > dp[i][1]:
                    dp[i] = (j, dp[j][1] + 1)
                    if max_v < dp[i][1]:
                        max_v = dp[i][1]
                        l = i

        result = []
        while l != -1:
            result.append(nums[l])
            l = dp[l][0]

        return result[::-1]
