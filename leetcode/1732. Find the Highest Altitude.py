class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        n = len(gain)
        altitudes = [0 for _ in range(n + 1)]

        max_v = float("-inf")

        for i in range(1, len(altitudes)):
            altitudes[i] = altitudes[i - 1] + gain[i - 1]
            max_v = max(max_v, altitudes[i])

        return max(max_v, altitudes[0])

        
