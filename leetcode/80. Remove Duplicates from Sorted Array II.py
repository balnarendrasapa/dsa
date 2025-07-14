class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        appeared = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                appeared += 1

            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                appeared = 1
                k += 1

            elif appeared < 3:
                nums[k] = nums[i]
                k += 1

        return k
