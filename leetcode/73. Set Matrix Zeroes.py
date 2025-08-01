class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = {}
        zero_columns = {}

        rows = len(matrix)
        columns = len(matrix[0])

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    zero_rows[i] = 9999
                    zero_columns[j] = 9999

        for i in zero_rows.keys():
            for j in range(columns):
                matrix[i][j] = 0

        for i in zero_columns.keys():
            for j in range(rows):
                matrix[j][i] = 0
