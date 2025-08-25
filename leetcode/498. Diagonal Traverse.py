class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])
        
        diagonals = defaultdict(list)

        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])

        result = []
        for key in diagonals.keys():
            if key % 2 == 0:
                result.extend(diagonals[key][::-1])
            else:
                result.extend(diagonals[key])

        return result

        
