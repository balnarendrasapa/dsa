from math import ceil

def getScore(piles, k):
    score = 0
    for p in piles:
        score += ceil(p / k)
    return score

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = 10**10

        while l < r:
            mid = (l + r) // 2
            score = getScore(piles, mid)

            if score <= h:
                r = mid
            else:
                l = mid + 1

        return l
