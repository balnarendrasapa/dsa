class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], -x[1]))

        pair_count = 0

        n = len(points)

        for i in range(n):
            upper_y = points[i][1]
            lower_limit_y = float("-inf")

            for j in range(i + 1, n):
                
                if points[j][1] <= upper_y and points[j][1] > lower_limit_y:
                    lower_limit_y = points[j][1]
                    pair_count += 1
                    if points[j][1] == upper_y:
                        break

        return pair_count
