class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        blocks = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                blocks[3 * (i // 3) + j // 3].add(board[i][j])

        def isValid(row, col, ch):
            
            block = 3 * (row // 3) + col // 3

            return (ch not in rows[row] 
                    and ch not in cols[col]
                    and ch not in blocks[block])
            
        def solve(row, col):
            if row == n:
                return True

            if col == n:
                return solve(row + 1, 0)

            if board[row][col] == ".":
                for i in range(1, 10):
                    if isValid(row, col, str(i)):
                        ch = str(i)
                        board[row][col] = ch
                        rows[row].add(ch)
                        cols[col].add(ch)
                        block = 3 * (row // 3) + (col // 3)
                        blocks[block].add(ch)

                        if solve(row, col + 1):
                            return True

                        board[row][col] = "."
                        rows[row].remove(ch)
                        cols[col].remove(ch)
                        blocks[block].remove(ch)

                return False
            else:
                return solve(row, col + 1)
        solve(0, 0)
