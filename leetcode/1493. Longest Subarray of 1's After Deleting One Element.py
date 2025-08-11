class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        one_start = 0
        zeroes = 0
        max_v = float("-inf")

        for one_end in range(len(nums)):
            if nums[one_end] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[one_start] == 0:
                    zeroes -= 1

                one_start += 1

            max_v = max(max_v, one_end - one_start + 1)

        return max_v - 1
