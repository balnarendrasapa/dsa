class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        start = 0
        current_sum = 0

        for end in range(n):
            current_sum += nums[end]
            
            while current_sum * (end - start + 1) >= k:
                current_sum -= nums[start]
                start += 1
            
            total += (end - start + 1)

        return total
