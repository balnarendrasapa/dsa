class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)

        rs = 0
        for i in range(len(nums)):
            if rs == s - rs - nums[i]:
                return i
            rs += nums[i]

        return -1
