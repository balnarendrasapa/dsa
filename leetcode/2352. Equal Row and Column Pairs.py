class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[0][i] == grid[j][0]:
                    check = False
                    for k in range(len(grid)):
                        if grid[k][i] != grid[j][k]:
                            check = True
                            break

                    if not check:
                        count += 1

        return count
