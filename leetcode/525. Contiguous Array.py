class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max_sum = 0
        count = 0
        k = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                count += -1
            elif nums[i] == 1:
                count += 1

            if count in k:
                max_sum = max(max_sum, i - k[count])
            else:
                k[count] = i

        return max_sum
