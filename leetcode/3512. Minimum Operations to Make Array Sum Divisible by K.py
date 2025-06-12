class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum_value = sum(nums)

        if sum_value < k:
            return sum_value

        return sum_value % k

