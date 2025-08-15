class Solution:
    def getArea(self, heights):
        n = len(heights)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        left[0] = -1
        right[n - 1] = n

        for i in range(1, n):
            prev = i - 1
            while prev >= 0 and heights[prev] >= heights[i]:
                prev = left[prev]
            left[i] = prev

        for i in range(n - 2, -1, -1):
            nex = i + 1
            while nex <= n - 1 and heights[nex] >= heights[i]:
                nex = right[nex]
            right[i] = nex

        area = float("-inf")
        for i in range(n):
            temp = (right[i] - left[i] - 1) * heights[i]
            area = max(area, temp)

        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = int(matrix[i][j]) + dp[i - 1][j]

        max_area = float("-inf")
        for row in dp:
            area = self.getArea(row)
            max_area = max(max_area, area)

        return max_area
