class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        start = 0
        end = 1
        v = 0
        while end < len(nums):
            while nums[end] - nums[start] > 1:
                start += 1
            if nums[end] - nums[start] == 1:
                v = max(end - start + 1, v)
            end += 1

        return v
