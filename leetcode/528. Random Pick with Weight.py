class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0

        for weight in w:
            total += weight
            self.prefix.append(total)

        self.total = total

    def pickIndex(self) -> int:
        
        r = random.randint(1, self.total)

        index = bisect.bisect_left(self.prefix, r)

        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
