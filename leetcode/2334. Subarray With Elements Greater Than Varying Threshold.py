from typing import List

class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.max_size = 0 

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            self.max_size = max(self.max_size, 1)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            self.max_size = max(self.max_size, self.size[rootY])
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.max_size = max(self.max_size, self.size[rootX])
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        vi = [(nums[i], i) for i in range(n)]  
        vi.sort(reverse=True) 
        dsu = DSU()
        active = [False] * n

        j = 0
        for k in range(1, n + 1):
            k_threshold = threshold / k
            while j < n and vi[j][0] > k_threshold:
                index = vi[j][1]
                active[index] = True
                dsu.find(index)
                if index - 1 >= 0 and active[index - 1]:
                    dsu.union(index, index - 1)
                if index + 1 < n and active[index + 1]:
                    dsu.union(index, index + 1)
                # After each new activation, check the largest component
                if dsu.get_size(index) >= k:
                    return k
                j += 1
        return -1
