class Solution:
    def dfs(self, isConnected, index, visited):
        for i in range(len(isConnected)):
            if not visited[i] and isConnected[index][i] == 1:
                visited[i] = True
                self.dfs(isConnected, i, visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        provinces = 0
        visited = [False for _ in range(m)]

        for i in range(m):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                self.dfs(isConnected, i, visited)
        
        return provinces
