class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdiff = -99999999

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j] and maxdiff < nums[j] - nums[i]:
                    maxdiff = nums[j] - nums[i]

        if maxdiff < 0:
            return -1

        return maxdiff
