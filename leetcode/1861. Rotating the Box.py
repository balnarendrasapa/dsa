class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        res = [["." for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][m - i - 1] = boxGrid[i][j]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i - 1 >= 0 and res[i][j] == "." and res[i - 1][j] == "#":
                    k = i
                    while k < n and res[k][j] == ".":
                        k += 1
                    res[i - 1][j], res[k - 1][j] = res[k - 1][j], res[i - 1][j]

        return res
