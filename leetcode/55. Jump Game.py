class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True

        i = n - 1
        while i >= 0:
            element = nums[i]
            j = i
            while j <= n - 1 and j <= i + element:
                if dp[j] == True:
                    dp[i] = True
                    break
                j += 1
            i -= 1

        return dp[0]
