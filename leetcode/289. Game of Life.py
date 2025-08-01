class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        switch = []
        rows = len(board)
        columns = len(board[0])

        for i in range(rows):
            for j in range(columns):
                count_ones = 0
                
                for dx, dy in [(1, 1), (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]:
                    if 0 <= i + dx <= rows - 1 and 0 <= j + dy <= columns - 1 and board[i + dx][j + dy] == 1:
                        count_ones += 1

                if board[i][j] == 1:
                    if count_ones < 2 or count_ones > 3:
                        switch.append([i, j])
                elif board[i][j] == 0:
                    if count_ones == 3:
                        switch.append([i, j])

        for i, j in switch:
            board[i][j] = 1 if board[i][j] == 0 else 0
