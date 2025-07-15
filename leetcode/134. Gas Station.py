class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        result = [gas[i] - cost[i] for i in range(n)]

        if sum(result) < 0:
            return -1

        c = 0
        s = 0
        for i in range(n):
            c += result[i]
            if c < 0:
                c = 0
                s = i + 1
        return s
