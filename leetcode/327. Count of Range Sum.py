class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, i, val):

        while i <= self.size:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i

        return s

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        prefix = [0]

        for i in nums:
            prefix.append(prefix[-1] + i)

        all_vals = set(prefix)

        for p in prefix:
            all_vals.add(p - lower)
            all_vals.add(p - upper)

        sorted_vals = sorted(all_vals)

        rank = {v:i+1 for i, v in enumerate(sorted_vals)}

        ft = FenwickTree(len(rank))

        result = 0
        for p in prefix:
            left = rank[p - upper]
            right = rank[p - lower]

            result += ft.query(right) - ft.query(left - 1)
            ft.update(rank[p], 1)

        return result
