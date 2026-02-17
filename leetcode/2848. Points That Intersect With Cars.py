class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        r = set()

        for s, e in nums:
            r.update(list(range(s, e + 1)))

        return len(r)
