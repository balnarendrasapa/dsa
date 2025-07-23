class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        x, y, dx, dy = 0, 0, 0, 1

        result = []
        for _ in range(rows * cols):
            result.append(matrix[x][y])
            matrix[x][y] = "."

            if not 0 <= y + dy < cols or not 0 <= x + dx < rows or matrix[x + dx][y + dy] == ".":
                dx, dy = dy, -dx

            x += dx
            y += dy

        return result


                
