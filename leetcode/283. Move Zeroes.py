class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        window_size = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                window_size += 1

            else:
                temp = nums[i]
                nums[i] = 0
                nums[i - window_size] = temp
