class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        resultant = []
        index = 0
        prev = 0
        while index < len(nums):
            index += 3
            resultant.append(nums[prev:index])
            prev = index

        for i in resultant:
            if abs(i[0] - i[1]) > k or abs(i[1] - i[2]) > k or abs(i[2] - i[0]) > k:
                return []
            
        return resultant
