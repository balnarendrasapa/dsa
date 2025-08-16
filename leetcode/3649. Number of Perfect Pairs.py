class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        nums = sorted(abs(x) for x in nums)
        count = 0
        n = len(nums)
        i = 0
        for j in range(n):
            while i < j and 2 * nums[i] < nums[j]:
                i += 1
            count += j - i
        return count
