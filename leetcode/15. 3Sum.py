class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res = set()
        nums.sort()
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
            i += 1

        return list(res)
