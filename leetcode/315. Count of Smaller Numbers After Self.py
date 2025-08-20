class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, i, delta):

        while i <= self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):

        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i

        return s

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []

        sorted_unique = sorted(set(nums))

        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}

        ft = FenwickTree(len(sorted_unique))

        res = []

        for i in reversed(nums):

            idx = rank[i]

            res.append(ft.query(idx - 1))

            ft.update(idx, 1)

        return res[::-1]
