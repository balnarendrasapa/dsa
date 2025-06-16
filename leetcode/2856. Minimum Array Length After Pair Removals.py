class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        p_i = 0
        p_j = (len(nums) + 1) // 2
        removed = [False] * len(nums)

        while p_i < (len(nums) + 1) // 2 and p_j < len(nums):
            if nums[p_i] < nums[p_j]:
                removed[p_i] = True
                removed[p_j] = True

            # elif nums[p_i] == nums[p_j]:
            #     p_j += 1
            
            p_i += 1
            p_j += 1


        count = 0
        for i in removed:
            if i == False:
                count += 1

        return count
