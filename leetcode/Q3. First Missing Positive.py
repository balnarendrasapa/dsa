class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(len(nums)):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct = nums[i] - 1
                nums[correct], nums[i] = nums[i], nums[correct]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
