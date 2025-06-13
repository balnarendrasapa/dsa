class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        if len(beans) == 1:
            return 0

        beans.sort()

        total = sum(beans)
        minimum = float("inf")
        n = len(beans)

        for i in range(n):
            remaining = beans[i] * (n - i)
            removed = total - remaining
            if removed < minimum:
                minimum = removed
        
        return minimum
