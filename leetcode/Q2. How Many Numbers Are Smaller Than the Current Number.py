class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        numsIndex = [(nums[i], i) for i in range(len(nums))]

        numsIndex.sort(key=lambda x: x[0])

        result = [0 for _ in nums]

        for index in range(len(numsIndex)):
            if index > 0 and numsIndex[index][0] == numsIndex[index - 1][0]:
                result[numsIndex[index][1]] = result[numsIndex[index - 1][1]]
            else:
                result[numsIndex[index][1]] = index

        return result
