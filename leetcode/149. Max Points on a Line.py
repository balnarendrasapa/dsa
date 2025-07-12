from collections import Counter

def getSlope(p1, p2):
    if p2[0] - p1[0] == 0:
        return float("inf")

    return float((p2[1] - p1[1]) / (p2[0] - p1[0]))

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        if n == 1 or n == 2:
            return n

        slopes = dict()
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                key = tuple(points[i])
                if key in slopes:
                    slopes[key].append(getSlope(points[i], points[j]))
                else:
                    slopes[key] = [getSlope(points[i], points[j])]

        print(slopes)
        v = -9999
        for key in slopes:
            c = Counter(slopes[key]).most_common(1)
            v = max(c[0][1], v)

        return v + 1
        
