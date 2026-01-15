class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def maxSpan(bars):
            bars.sort()

            maxV = 1
            streak = 1

            for i in range(1, len(bars)):
                if bars[i] - bars[i - 1] == 1:
                    streak += 1
                else:
                    streak = 1

                maxV = max(maxV, streak)

            return maxV + 1
        
        return min(maxSpan(hBars), maxSpan(vBars)) ** 2
