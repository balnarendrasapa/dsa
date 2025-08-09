class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        ans = nums[0]

        for num in nums:
            temp = (num, num * curMax, num * curMin)
            curMax = max(temp)
            curMin = min(temp)

            ans = max(ans, curMax)

        return ans
