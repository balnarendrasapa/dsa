def checkDuplicates(l):
    temp = []

    for i in l:
        if i != ".":
            if i not in temp:
                temp.append(i)
            else:
                return True
    
    return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            if checkDuplicates(row):
                return False

        for i in range(len(board[0])):
            temp_col = [board[j][i] for j in range(len(board[0]))]
            if checkDuplicates(temp_col):
                return False
            
        for i in range(0, len(board), 3):
            rows = board[i:i+3]

            for j in range(0, len(rows[0]), 3):
                temp = []
                for k in rows:
                    temp.extend(k[j:j+3])
                if checkDuplicates(temp):
                    return False

        return True
