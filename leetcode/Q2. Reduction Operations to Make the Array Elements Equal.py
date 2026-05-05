class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        i = n - 1

        result = 0
        while i >= 1:
            if nums[i - 1] != nums[i]:
                result += n - i

            i -= 1

        return result
