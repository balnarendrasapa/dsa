class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = dict()

        def getPerms(nums, perm):
            if len(nums) == 1:
                result[tuple(perm + [nums[0]])] = 0
                return

            for i in range(len(nums)):
                getPerms(nums[:i] + nums[i + 1:], perm + [nums[i]])

        getPerms(nums, [])
        return list(result.keys())
