from collections import deque

class Solution:
    def getBIndex(self, index, n):
        div = (index - 1) // n
        row = n - div - 1
        col = (index - 1) % n if div % 2 == 0 else n - (index - 1) % n - 1
        return row, col

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        que = deque([(1, 0)])
        visited = set([1])
        target = n * n

        while que:
            idx, moves = que.popleft()

            for i in range(1, 7):
                nxt = idx + i

                if nxt > target:
                    break

                r, c = self.getBIndex(nxt, n)
                if board[r][c] != -1:
                    nxt = board[r][c]

                if nxt == target:
                    return moves + 1

                if nxt not in visited:
                    visited.add(nxt)
                    que.append((nxt, moves + 1))

        return -1


            


        
        
