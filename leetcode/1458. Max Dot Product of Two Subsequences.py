class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        m = len(nums1)
        n = len(nums2)

        dp = [[float("-inf") for i in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr_prod = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + curr_prod, curr_prod)

        return dp[-1][-1]
        
