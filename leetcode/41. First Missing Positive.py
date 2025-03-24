class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = len(nums)

        if max_num == 0:
            return 1

        temp = [False] * max_num

        for j in nums:
            if 0 < j <= max_num:
                temp[j - 1] = True

        for i in range(len(temp)):
            if temp[i] == False:
                return i + 1
        
        return max_num + 1
