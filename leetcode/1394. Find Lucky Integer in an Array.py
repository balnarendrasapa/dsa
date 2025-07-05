from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        k = Counter(arr)

        max_v = -1
        for key in k.keys():
            if key == k[key]:
                max_v = max(max_v, key)

        return max_v
