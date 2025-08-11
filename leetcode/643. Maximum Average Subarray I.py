class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_start = 0
        window_end = k - 1

        s = 0
        for num in nums[window_start:window_end + 1]:
            s += num

        max_v = s
        window_end += 1
        while window_end < len(nums):
            s -= nums[window_start]
            s += nums[window_end]

            max_v = max(max_v, s)
            window_start += 1
            window_end += 1

        return max_v / k
