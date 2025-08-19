class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        result = [[0 for _ in range(n)] for _ in range(n)]

        x, y = 0, 0
        dx, dy = 0, 1
        val = 1

        while val != n * n + 1:
            result[x][y] = val
            val += 1

            if x + dx == n or y + dy == n or result[x + dx][y + dy] != 0:
                dx, dy = dy, -dx

            x = x + dx
            y = y + dy
            
        
        return result
