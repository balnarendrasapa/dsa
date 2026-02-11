class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        n = len(intervals)
        starts = [(intervals[i][0], i) for i in range(n)]

        starts.sort()
        starts_val = [s[0] for s in starts]
        res = [-1] * n
        for i in range(n):
            end = intervals[i][1]
            position = bisect.bisect_left(starts_val, end)
            if position < n:
                res[i] = starts[position][1]

        return res
