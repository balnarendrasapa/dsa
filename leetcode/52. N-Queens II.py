class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def isSafe(row, col, board):
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False

                i -= 1
                j -= 1

            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False

                i -= 1
                j += 1

            return True

        def backtrack(row):
            nonlocal result
            if row == n:
                result += 1
                return
            
            else:
                for col in range(n):
                    if isSafe(row, col, board):
                        board[row][col] = "Q"
                        backtrack(row + 1)
                        board[row][col] = "."

        board = [["." for _ in range(n)] for _ in range(n)]
        result = 0
        backtrack(0)
        return result
