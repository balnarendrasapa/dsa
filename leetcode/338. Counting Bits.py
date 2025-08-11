class Solution:
    def getSetBitCount(self, n):

        count = 0
        while n:
            count += n & 1
            n = n >> 1

        return count

    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(self.getSetBitCount(i))

        return result
