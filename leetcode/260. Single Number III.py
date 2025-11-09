from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = Counter(nums)

        R = []
        for key in d.keys():
            if d[key] == 1:
                R.append(key)

        return R
