class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, left, right):
        if left == right:
            self.tree[node] = nums[left]
            return

        mid = (left + right) // 2
        self.build(nums, 2 * node + 1, left, mid)
        self.build(nums, 2 * node + 2, mid + 1, right)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index: int, val: int) -> None:
        self._update(0, 0, self.n - 1, index, val)

    def _update(self, node, left, right, index, val):
        if left == right:
            self.tree[node] = val
            return
        
        mid = (left + right) // 2

        if index <= mid:
            self._update(2 * node + 1, left, mid, index, val)
        else:
            self._update(2 * node + 2, mid + 1, right, index, val)

        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def sumRange(self, left: int, right: int) -> int:
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, left, right, ql, qr):
        if qr < left or ql > right:
            return 0

        if ql <= left and right <= qr:
            return self.tree[node]

        mid = (left + right) // 2

        return self._query(2 * node + 1, left, mid, ql, qr) + self._query(2 * node + 2, mid + 1, right, ql, qr)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
