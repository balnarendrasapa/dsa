from collections import deque

def bfs(visited, i, j, m, n, grid):

    stack = deque([])
    stack.append([i, j])
    visited[i][j] = True

    while stack:
        index = stack.popleft()

        if index[1] - 1 >= 0 and grid[index[0]][index[1] - 1] == "1" and visited[index[0]][index[1] - 1] == False:
            stack.append([index[0], index[1] - 1])
            visited[index[0]][index[1] - 1] = True
        
        if index[1] + 1 < n and grid[index[0]][index[1] + 1] == '1' and visited[index[0]][index[1] + 1] == False:
            stack.append([index[0], index[1] + 1])
            visited[index[0]][index[1] + 1] = True
        
        if index[0] - 1 >= 0 and grid[index[0] - 1][index[1]] == '1' and visited[index[0] - 1][index[1]] == False:
            stack.append([index[0] - 1, index[1]])
            visited[index[0] - 1][index[1]] = True
        
        if index[0] + 1 < m and grid[index[0] + 1][index[1]] == '1' and visited[index[0] + 1][index[1]] == False:
            stack.append([index[0] + 1, index[1]]) 
            visited[index[0] + 1][index[1]] = True

    return visited   


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == '1':
                    count += 1
                    visited = bfs(visited, i, j, m, n, grid)

        return count
