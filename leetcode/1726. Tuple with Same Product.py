from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d[nums[i] * nums[j]] += 1

        count = 0
        for key in d.keys():
            if d[key] != 1:
                count += d[key] * (d[key] - 1) * 4

        return count
