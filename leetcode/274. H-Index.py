class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i in range(n):
            difference = n - i
            if difference <= citations[i]:
                return difference

        return 0
