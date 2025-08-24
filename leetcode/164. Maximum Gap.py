class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        max_v = 0
        for i in range(1, len(nums)):
            max_v = max(max_v, nums[i] - nums[i - 1])

        return max_v
