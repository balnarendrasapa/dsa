MAX_RANGE = (10**6) + 1
prime = [True] * MAX_RANGE
prime[0] = prime[1] = False

for i in range(2, int(sqrt(MAX_RANGE))):
    if prime[i] == True:
        for j in range(i*i, MAX_RANGE, i):
            prime[j] = False

from collections import defaultdict, deque
import heapq

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        val_to_ind = defaultdict(list)

        for i, val in enumerate(nums):
            val_to_ind[val].append(i)

        q = deque([0])
        visited = [False] * n
        visited[0] = True
        used_prime = set()
        steps = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node == n - 1:
                    return steps

                for nei in (node - 1, node + 1):
                    if 0 <= nei < n and not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

                val = nums[node]
                if prime[val] and val not in used_prime:
                    for multiple in range(val, MAX_RANGE, val):
                        if multiple in val_to_ind:
                            for nei in val_to_ind[multiple]:
                                if not visited[nei]:
                                    visited[nei] = True
                                    q.append(nei)

                    used_prime.add(val)

            steps +=1
        
        return -1

        
