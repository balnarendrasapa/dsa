from collections import deque

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        el = len(matrix)

        top = 0
        bottom = el - 1

        # vertical reverse
        while top < bottom:
            for i in range(el):
                matrix[top][i], matrix[bottom][i] = matrix[bottom][i], matrix[top][i]

            top += 1
            bottom -= 1

        # transpose
        for row in range(el):
            for col in range(row + 1, el):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        return matrix
