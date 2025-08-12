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

# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         mp1=defaultdict(int)
#         mp2=defaultdict(int)


#         for r in grid:
#             mp1[tuple(r)]+=1
        
#         for i in range(len(grid)):
#             for j in range(i+1,len(grid[0])):
#                 grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
        
#         for c in grid:
#             mp2[tuple(c)]+=1
        
#         count=0
#         for row in mp1:
#             if row in mp2:
#                 count+=mp1[row]*mp2[row]
#         return count
