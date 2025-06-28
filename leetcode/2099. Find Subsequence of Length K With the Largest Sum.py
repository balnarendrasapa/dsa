class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp = [[nums[i], i] for i in range(len(nums))]

        temp.sort(key=lambda x: x[0])

        result = temp[-k:]

        result.sort(key=lambda x: x[1])
        
        return [i[0] for i in result]
