def maxarr(nums, arr, index):
    if index > 0 and  index < len(nums):
        arr[index] = max(maxarr(nums, arr, index - 1) + nums[index], nums[index])
        return arr[index]
    if index == 0:
        arr[0] = nums[0]
        return nums[0]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [0] * len(nums)
        K = maxarr(nums, arr, len(nums) - 1)
        print(arr)
        return max(arr)
                
        
