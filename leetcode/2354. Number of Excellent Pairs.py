class Solution:
    def getSetCount(self, num):
        result = 0
        while num:
            result += num & 1
            num = num >> 1

        return result

    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        set_array = [self.getSetCount(num) for num in nums]

        set_array.sort()

        n = len(set_array)
        l = 0
        r = n - 1
        result = 0

        while l < n and r >= 0:
            if set_array[l] + set_array[r] < k:
                l += 1
            else:
                result += (n - l)
                r -= 1

        return result
        
